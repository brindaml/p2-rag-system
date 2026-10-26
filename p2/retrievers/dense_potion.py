"""Ablation: dense with potion-retrieval-32M in place of bge-small, everything else unchanged.

The one change is the embedding model; the chunks, the cosine scoring and the best-chunk lift to
documents are dense.py's. The file name tells p2 score that it varies dense.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers.dense import Dense

NEEDS_CLAUDE = False
BASE = "dense"


class DensePotion(Dense):
    model = embed.POTION


def build(corpus, cfg):
    return DensePotion(corpus, cfg)
