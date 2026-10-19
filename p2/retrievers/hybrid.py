"""Hybrid retrieval (stage 1): reciprocal rank fusion of bm25 and dense.

Ported from the 13 lab's rrf() (pipeline.py): each document scores the sum of 1 / (60 + rank) over
the two full rankings, so a document both systems rank well beats one that only a single system likes.
Ranks are looked up in a dict rather than with list.index(), which would scan the list per document.
search_chunks does the same fusion over chunk rankings, so `p2 answer` works with hybrid.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

RRF_K = 60
SYSTEMS = ("bm25", "dense")


def rrf(rankings: list[list[tuple[str, float]]], k: int = RRF_K) -> list[tuple[str, float]]:
    """Fuse full rankings of (id, score) pairs, best first; equal fused scores in id order."""
    fused: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, _) in enumerate(ranking, 1):
            fused[item] = fused.get(item, 0.0) + 1 / (k + rank)
    return order(fused.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.systems = [retrievers.build(name, corpus, cfg) for name in SYSTEMS]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(self.systems[0].chunks)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([s.search(text, self.n_docs) for s in self.systems])[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([s.search_chunks(text, self.n_chunks) for s in self.systems])[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
