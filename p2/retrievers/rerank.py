"""Reranking (stage 1): Claude reorders hybrid's top 20, one claude -p call per query.

Ported from the 13 lab's rerank_one() (pipeline.py): the top 20 go to Claude as numbered passages
(each cut to its first 600 characters, as in the lab), and the schema forces the reply into
{"order": [20 numbers]}, each between 1 and 20. A reply that is not each number once, or a failed
call, keeps hybrid's order. Everything below the 20 keeps hybrid's order underneath.
Every call goes through p2.claude.call, which caches replies and records tokens in the trace.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers

NEEDS_CLAUDE = True

FIRST_STAGE = "hybrid"
CANDIDATES = 20
PASSAGE_CHARS = 600

SCHEMA = {
    "type": "object",
    "properties": {
        "order": {
            "type": "array",
            "items": {"type": "integer", "minimum": 1, "maximum": CANDIDATES},
            "minItems": CANDIDATES,
            "maxItems": CANDIDATES,
        }
    },
    "required": ["order"],
}

PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


class Rerank:
    model: str | None = None

    def __init__(self, corpus, cfg):
        self.cfg = cfg
        self.model = cfg.model
        self.first = retrievers.build(FIRST_STAGE, corpus, cfg)
        self.n_docs = len(corpus.docs)
        self.doc_text = {docid: doc.text for docid, doc in corpus.docs.items()}
        self.chunk_text = {c.id: c.text for c in self.first.systems[0].chunks}
        self.n_chunks = len(self.chunk_text)

    def rerank(self, query: str, ids: list[str], text_of: dict[str, str]) -> list[str]:
        """The top CANDIDATES of ids in Claude's order, then the rest in their first-stage order."""
        top, rest = ids[:CANDIDATES], ids[CANDIDATES:]
        passages = "\n\n".join(f"[{i}] {text_of[d][:PASSAGE_CHARS]}" for i, d in enumerate(top, 1))
        prompt = PROMPT.format(n=len(top), query=query, passages=passages)
        reply = claude.call(prompt, SCHEMA, model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        order = (reply.output or {}).get("order")
        if reply.error or not isinstance(order, list) or sorted(order) != list(range(1, len(top) + 1)):
            print(f"rerank: kept {FIRST_STAGE}'s order for {query[:60]!r}: {reply.error or order}", file=sys.stderr)
            return ids
        return [top[i - 1] for i in order] + rest

    def _scored(self, ids: list[str], k: int) -> list[tuple[str, float]]:
        # Scores from position, so they fall strictly and the file keeps this order.
        return [(d, float(len(ids) - pos)) for pos, d in enumerate(ids[:k])]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ids = [d for d, _ in self.first.search(text, self.n_docs)]
        return self._scored(self.rerank(text, ids, self.doc_text), k)

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ids = [c for c, _ in self.first.search_chunks(text, self.n_chunks)]
        return self._scored(self.rerank(text, ids, self.chunk_text), k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
