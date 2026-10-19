"""Dense retrieval (stage 1): embed every chunk once with bge-small, embed the query, rank chunks by cosine similarity.

Ported from the 12 lab's dense_rankings (retrieve.py): one matrix product scores every chunk against
the query. The vectors from p2/embed.py are unit length, so the dot product is the cosine similarity.
The chunk vectors are cached in .cache/vectors/, so only the first run on a corpus encodes it.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    model = embed.BGE

    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)  # one row per chunk

    def score_chunks(self, text: str) -> list[float]:
        if not self.chunks:
            return []
        query = self.embedder.encode([text])[0]
        return (self.vectors @ query).tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
