# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

For dense, the embedding model was the bge small because it was measured to be stronger. The documents were chunked into 300 words chunks. Nothing was fused, there was no reranker, and the changes are that it is scoring the actual chunks instead of the article. The document is as good as its best chunk. 

For hybrid, bge small was reused, the chunking was the same, and what was fused was bm25 and dense. They were fused with the reciprocal rank fusion, where it gets a hybrid score from both its bm25 rank and dense rank, taken as a reciprocal of 1/(60+rank) and those are added together, and then are sorted from that. There was no reranker, and the changes from the lab were that the ranks are used in a dict instead of a list.index, making it faster.

For rerank, there wasn't a specific embedding model because it just reranked from hybrid, so bm25 and bge small. The chunk was done the same way with 300 word chunks, nothing was fused because it just used hybrid's fused rankings. The reranker candidates  were the top 20 from hybrid, where everything below the top 20 was kept in hybrid's original order. Claude is the one that reorders the top 20. The changes were that the schema required all numbers to be between 1-20 and that anything invalid went back to the hybrid's original order.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.758 | 0.800 | 0.750 |
| rerank_c10 | 0.592 | 0.700 | 0.604 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.688 | 0.626 | 0.966 |
| rerank_c10 | Recall@10 | 0.500 | 0.405 | 0.917 |
| rerank_c10 | MRR@10 | 0.571 | 0.571 | 1.000 |
| rerank_c10 | nDCG@10 | 0.484 | 0.440 | 0.936 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.231 | [+0.001, +0.451] | 0.327 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.270 | [+0.131, +0.426] | 0.216 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.306 | [+0.179, +0.437] | 0.187 | rerank higher |
| rerank_c10 minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| rerank_c10 minus bm25 | MRR@10 | +0.193 | [-0.065, +0.444] | 0.366 | not distinguishable |
| rerank_c10 minus bm25 | nDCG@10 | +0.086 | [-0.151, +0.316] | 0.339 | not distinguishable |
| rerank_c10 minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| rerank_c10 minus dense | MRR@10 | +0.138 | [-0.058, +0.333] | 0.288 | not distinguishable |
| rerank_c10 minus dense | nDCG@10 | +0.125 | [-0.051, +0.290] | 0.248 | not distinguishable |
| rerank_c10 minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| rerank_c10 minus hybrid | MRR@10 | +0.229 | [+0.059, +0.406] | 0.251 | rerank_c10 higher |
| rerank_c10 minus hybrid | nDCG@10 | +0.161 | [+0.054, +0.276] | 0.161 | rerank_c10 higher |
| rerank_c10 minus rerank | Recall@10 | -0.167 | [-0.292, -0.058] | 0.166 | rerank higher |
| rerank_c10 minus rerank | MRR@10 | -0.100 | [-0.225, +0.000] | 0.164 | not distinguishable |
| rerank_c10 minus rerank | nDCG@10 | -0.146 | [-0.264, -0.044] | 0.159 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

The differences that are distinguishable from zero are that rerank is higher than hybrid and dense, and rerank is also higher than bm25 on MRR@10 and nDCG@10. It is not distinguishable from bm25 on recall@10. bm25, dense, and hybrid cannot be told apart from each other. 

The minimum detectable difference at 20 queries ranges from 0.166 to 0.415. This means that anything smaller than that will be hard to detect with just 20 queries, they still might exist but you would need more than 20 queries to prove this.

Lecture 12 shows that bm25 and dense will miss a couple of predictable queries, which is what happened. All of the paraphrase queries for bm25 and most of the identifier queries for dense were missed, but the sample size was small. Additionally lecture 13 showed that an LLM reranker can improve rankings, which is what happened. However, lecture 13 said that fusion helps with a weaker partner and hurts a strong retriever, but for these tests hybrid wasn't distinguishable from bm25 and dense, leaving this open.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 12 of 12 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

The system that answered was rerank, because it was the system that did the best out of all of them. 
I did not change anything in prompts/answer.txt, so everything 8/8 were verified and 4/4 were declined. 

For a02, the quote really does support the claim next to it.
For a04, the quote really does support the claim.
For a07, the quote really does support the claim as well.

TODO: double-check the audit before submitting: cover both claims in a04 and a07, and give a reason for each verdict.


---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My corpus is a total of 226 Wikipedia articles all around Pokemon, dedicated to the games, its spinoffs, the characters, the species,  and just general information that was all available from Wikipedia's API. It is a total of 2.5 MB. The license basis for publishing it is CC BY-SA 4.0 all from Wikipedia's URL, and p2 license reported all of the articles as ok.

I was the least sure about the Pokemon Go article, it was by far the longest article and I wasn't sure it was too much information condensed into one article that could cloud and confuse queries. I decided to keep it because it wasn't split as it was under 15,000 words, and I thought the information would be valuable to be able to reference.

This comes from the brief list that states "CC0, CC BY and CC BY-SA text, including Wikipedia (CC BY-SA 4.0, with attribution)" 


### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

There were 35 queries total, 10 by hand and 25 from claude. The queries were divided into 11 identifier, 17 paraphrase, and 7 mixed. I focused a lot on paraphrase questions because that is what my ablation hypothesis was about, so I wanted to see what it would do with such a wide variety of information, but not a specific question. 
I decided a document was relevant if the snippet justification fully answered the question I was asking, not whether or not the actual article was specific to the question. This was important because these documents are related, so the system doesn't need to necessarily find the exact article to be able to find correct information, so it was based largely on if it contained the answer using the snippets.
The candidates were found via the top 5 of bm25, dense, and hybrid, and they were added to a checklist with all of the snippets. I read all of the snippets before labeling, and if none of the documents were relevant, I added in documents that pointed to the answers, like snorlax and team_rocket.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.933 | 0.840 | 0.858 |
| dense | 0.779 | 0.706 | 0.703 |
| hybrid | 0.914 | 0.839 | 0.849 |
| rerank | 0.971 | 0.971 | 0.963 |
| ablation/dense_potion | 0.736 | 0.646 | 0.661 |

35 judged queries; nDCG uses binary labels; a random ranking of the 226 documents would get recall@10 near 0.044.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=11) | paraphrase (n=17) | mixed (n=7) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.863 | 1.000 |
| bm25 | MRR@10 | 0.939 | 0.770 | 0.857 |
| bm25 | nDCG@10 | 0.939 | 0.790 | 0.895 |
| dense | Recall@10 | 0.841 | 0.647 | 1.000 |
| dense | MRR@10 | 0.909 | 0.492 | 0.905 |
| dense | nDCG@10 | 0.847 | 0.517 | 0.929 |
| hybrid | Recall@10 | 1.000 | 0.824 | 1.000 |
| hybrid | MRR@10 | 1.000 | 0.668 | 1.000 |
| hybrid | nDCG@10 | 0.970 | 0.709 | 1.000 |
| rerank | Recall@10 | 1.000 | 0.941 | 1.000 |
| rerank | MRR@10 | 1.000 | 0.941 | 1.000 |
| rerank | nDCG@10 | 0.989 | 0.931 | 1.000 |
| ablation/dense_potion | Recall@10 | 0.886 | 0.529 | 1.000 |
| ablation/dense_potion | MRR@10 | 0.864 | 0.359 | 1.000 |
| ablation/dense_potion | nDCG@10 | 0.850 | 0.399 | 1.000 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=25) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.867 | 0.960 | -0.093 | [-0.327, +0.080] | not distinguishable |
| bm25 | MRR@10 | 0.658 | 0.913 | -0.255 | [-0.502, -0.010] | claude higher |
| bm25 | nDCG@10 | 0.707 | 0.919 | -0.212 | [-0.436, +0.001] | not distinguishable |
| dense | Recall@10 | 0.600 | 0.850 | -0.250 | [-0.580, +0.080] | not distinguishable |
| dense | MRR@10 | 0.533 | 0.774 | -0.241 | [-0.567, +0.089] | not distinguishable |
| dense | nDCG@10 | 0.538 | 0.769 | -0.232 | [-0.546, +0.084] | not distinguishable |
| hybrid | Recall@10 | 0.800 | 0.960 | -0.160 | [-0.420, +0.080] | not distinguishable |
| hybrid | MRR@10 | 0.750 | 0.874 | -0.124 | [-0.410, +0.136] | not distinguishable |
| hybrid | nDCG@10 | 0.761 | 0.885 | -0.123 | [-0.403, +0.118] | not distinguishable |
| rerank | Recall@10 | 0.900 | 1.000 | -0.100 | [-0.300, +0.000] | not distinguishable |
| rerank | MRR@10 | 0.900 | 1.000 | -0.100 | [-0.300, +0.000] | not distinguishable |
| rerank | nDCG@10 | 0.900 | 0.988 | -0.088 | [-0.295, +0.023] | not distinguishable |
| ablation/dense_potion | Recall@10 | 0.650 | 0.770 | -0.120 | [-0.440, +0.190] | not distinguishable |
| ablation/dense_potion | MRR@10 | 0.567 | 0.677 | -0.111 | [-0.437, +0.218] | not distinguishable |
| ablation/dense_potion | nDCG@10 | 0.591 | 0.689 | -0.098 | [-0.421, +0.222] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.110 | +0.267 | -0.157 | [-0.473, +0.130] | not distinguishable |
| MRR@10 | +0.139 | +0.125 | +0.014 | [-0.348, +0.358] | not distinguishable |
| nDCG@10 | +0.149 | +0.169 | -0.020 | [-0.348, +0.289] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.83 (10 queries), claude 0.91 (25 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 25 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.155 | [-0.293, -0.021] | 0.198 | bm25 higher |
| dense minus bm25 | MRR@10 | -0.135 | [-0.278, +0.002] | 0.205 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.155 | [-0.285, -0.028] | 0.189 | bm25 higher |
| hybrid minus bm25 | Recall@10 | -0.019 | [-0.105, +0.067] | 0.127 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.002 | [-0.089, +0.088] | 0.127 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.009 | [-0.081, +0.065] | 0.105 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.136 | [+0.043, +0.250] | 0.156 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.133 | [+0.042, +0.238] | 0.144 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.146 | [+0.060, +0.243] | 0.133 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.038 | [-0.038, +0.133] | 0.126 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.131 | [+0.040, +0.236] | 0.143 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.105 | [+0.019, +0.204] | 0.134 | rerank higher |
| rerank minus dense | Recall@10 | +0.193 | [+0.079, +0.321] | 0.182 | rerank higher |
| rerank minus dense | MRR@10 | +0.266 | [+0.137, +0.405] | 0.196 | rerank higher |
| rerank minus dense | nDCG@10 | +0.260 | [+0.140, +0.390] | 0.183 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.057 | [+0.000, +0.143] | 0.112 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.133 | [+0.040, +0.240] | 0.146 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.114 | [+0.031, +0.213] | 0.132 | rerank higher |
| ablation/dense_potion minus bm25 | Recall@10 | -0.198 | [-0.345, -0.057] | 0.209 | bm25 higher |
| ablation/dense_potion minus bm25 | MRR@10 | -0.195 | [-0.342, -0.052] | 0.210 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.197 | [-0.335, -0.065] | 0.196 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | -0.043 | [-0.171, +0.071] | 0.176 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | -0.060 | [-0.212, +0.092] | 0.220 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | -0.042 | [-0.184, +0.091] | 0.197 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.179 | [-0.307, -0.071] | 0.171 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.193 | [-0.312, -0.088] | 0.163 | hybrid higher |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.188 | [-0.304, -0.087] | 0.158 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.236 | [-0.371, -0.114] | 0.192 | rerank higher |
| ablation/dense_potion minus rerank | MRR@10 | -0.326 | [-0.473, -0.188] | 0.209 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.302 | [-0.444, -0.172] | 0.199 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

What is distinguishable is that rerank and hybrid beat dense and that rerank also beat bm25 and hybrid. However hybrid vs. bm25 is not distinguishable and neither is bm25 vs dense. This was all for 35 queries, and the MDD for that is about 0.11 to 0.22.

Between the hand and claude queries, both tell the story that rerank is the highest and that dense and potion are the lowest. The difference is that bm25 for hand is ranked lower than it is by claude. 

My prediction from prompt 1 did not hold, I thought that bm25 would do pretty bad but it did pretty well. I think this is because while pokemon and characters have similar traits, they have unique names and places and backstory that make it a lot easier to separate them. Also hybrid was not distinguishable from bm25, so that cannot be said.


---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

Hypothesis (written before the run): I believe that the potion will score lower than the bge with paraphrase questions because potion ignores context, which is difficult with a corpus as complex as Pokemon information.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_potion minus bm25 | Recall@10 | -0.198 | [-0.345, -0.057] | 0.209 | bm25 higher |
| ablation/dense_potion minus bm25 | MRR@10 | -0.195 | [-0.342, -0.052] | 0.210 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.197 | [-0.335, -0.065] | 0.196 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | -0.043 | [-0.171, +0.071] | 0.176 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | -0.060 | [-0.212, +0.092] | 0.220 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | -0.042 | [-0.184, +0.091] | 0.197 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | -0.179 | [-0.307, -0.071] | 0.171 | hybrid higher |
| ablation/dense_potion minus hybrid | MRR@10 | -0.193 | [-0.312, -0.088] | 0.163 | hybrid higher |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.188 | [-0.304, -0.087] | 0.158 | hybrid higher |
| ablation/dense_potion minus rerank | Recall@10 | -0.236 | [-0.371, -0.114] | 0.192 | rerank higher |
| ablation/dense_potion minus rerank | MRR@10 | -0.326 | [-0.473, -0.188] | 0.209 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.302 | [-0.444, -0.172] | 0.199 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_potion against dense (BASE = "dense" in p2/retrievers/dense_potion.py): it helped 5 queries, hurt 8 and left 22 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_potion RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| h05 | identifier | hand | 0.000 | 1.000 | +1.000 | helped |
| c21 | paraphrase | claude | 0.111 | 1.000 | +0.889 | helped |
| c07 | paraphrase | claude | 0.250 | 1.000 | +0.750 | helped |
| h04 | mixed | hand | 0.333 | 1.000 | +0.667 | helped |
| h10 | paraphrase | hand | 0.000 | 0.167 | +0.167 | helped |
| c10 | identifier | claude | 1.000 | 0.000 | -1.000 | hurt |
| c13 | paraphrase | claude | 1.000 | 0.000 | -1.000 | hurt |
| h03 | paraphrase | hand | 1.000 | 0.000 | -1.000 | hurt |
| c19 | paraphrase | claude | 1.000 | 0.125 | -0.875 | hurt |
| c04 | paraphrase | claude | 1.000 | 0.333 | -0.667 | hurt |
| h01 | identifier | hand | 1.000 | 0.500 | -0.500 | hurt |
| c11 | paraphrase | claude | 0.500 | 0.143 | -0.357 | hurt |
| c15 | paraphrase | claude | 0.500 | 0.333 | -0.167 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

I changed the embedding model in dense to use potion-retrieval-32M instead of bge-small-en-v1.5. What happened between them is that overall, MRR@10 went from 0.706 to 0.646. This was broken down to paraphrase: 0.492 vs 0.359 (highest drop), identifier: 0.909 vs 0.864, and mixed: 0.905 vs 1.000.
Unfortunately, the interval is not distinguishable, because it is from -.212 to .092. This does suggest that potion is lower mainly on paraphrasing, as my hypothesis had suggested, but this cannot be confirmed from the data. 
The MDD was 0.220, and the gap was only 0.060, so I definitely needed more queries to be able to see a gap this small. 
My changes explain some of the results from the queries. I suspected that because potion ignores the context, it would perform worse, and for example for h03, it read the word yellow and instead of matching that with a Pokemon (which was implied in context) it just matched the word itself. This happened again at c13, where it ignored the context and just matched "Mew", leaving the film part of the question out of it. It doesn't explain c21, where potion did better and found team rocket instantly, but it could be because of key words like "crime" that helped to support it. 



---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| h09 | rerank returned team_skull, pokemon_colosseum, and pokemon_xd-_gale_of_darkness | The ones that were relevant were team_rocket, pokemon_firered_and_leafgreen and pokemon_heartgold_and_soulsilver | This is likely because of the lack of detail, there are a lot of villains in the Pokemon universe and without names or further specifications it was hard to pull the exact one I was thinking of. | Next time, I would try putting in more detail without giving away the answer, maybe a catch phrase or other relevant part of the villain to help guide the question more. |
| c08 | pokemon_legends-_arceus, kleavor, arceus | arceus, kleavor, pokemon_diamond_and_pearl, and pokemon_legends-_arceus which was added later | This was a wrong label, the top result was correct as it states the region, just very briefly. The gold set failed here, not the system. | I need to be more careful about checking topics before labeling instead of just looking at snippets. |
| h08 | bm25 returned tetris_attack, puzzle_league, planet_puzzle_league | snorlax | The words road and blocking were never used in the article for snorlax, even though his description as a pokemon matched, it didn't match those words. Rerank got this, but not bm25. | I would try to be more specific in the query |
| c11 | bm25 returned pokemon_x_and_y, pokemon_platinum, pokemon_video_game_series_competitive_play| pokemon_unite | Vocab mismatch, the query used the word five instead of the number 5 | Being verbose and accomdating to multiple styles of writing (numerical and words) |
| h02 | bm25 returned mewtwo, dragonite, charizard | charizard | the word evolved and Pokemon is used frequently in other articles | Trying for specific differentiating words that would separate similar answers |
| c16 | bm25 returned pokemon_ranger, pokemon_the_movie-_diancie_and_the_cocoon_of_destruction, lucario | lucario | Vocab mismatch, the query used the word control instead of manipulate | Being intentional about vocabulary used in queries when there are a lot of possible matches |


Overall, the pattern is that it is important to be very clear in paraphrase queries because there were a lot of mismatches there. This makes sense, because with bm25 the system is looking for specific words, you must be explicit and not ambiguous on what you are trying to look for. I looked specifically at bm25 because rerank had only failed once, the other time it failed was my fault because of the gold set. 

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

The winner did not change, rerank was first on both by a distinguishably large amount. However, originally bm25, dense, and hybrid were tied, but for the Pokemon ones, hybrid beat dense and bm25 beat dense on recall.
This is likely because of a couple reasons, one being that the unique names in Pokemon favor bm25. This is kind of tested on the identifier queries, where bm25 was at 1.0, but the exact reason why isn't tested. Additionally, for the claude queries there was a lot more specific language copied from the articles, which made it easier to find exact wording, vs the human ones had more ambiguous vocabulary, but this led to a not distinguishable answer. 
With 20 queries, bm25, vs dense vs hybrid was not distinguishable because the gaps were smaller than the MDD of 0.17 to 0.42. 
With the 35 queries, the MDD was 0.11 to 0.22 and the potion gap was below it at 0.060.


---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 162,094 | 4,341 | 135.5 | 13,508 | 362 | 11.3 |
| traces/own-own-rerank.jsonl | rerank | 35 | 35 | 0 | 324,637 | 3,289 | 108.7 | 9,275 | 94 | 3.1 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 184,323 | 2,174 | 98.4 | 9,216 | 109 | 4.9 |
| traces/shared-practice-rerank_c10.jsonl | rerank_c10 | 20 | 20 | 2 | 118,721 | 1,764 | 60.7 | 5,936 | 88 | 3.0 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 375,262 | 4,082 | 186.7 | 9,382 | 102 | 4.7 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 9,216 | 4.9 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 9,216 | 4.9 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 9,216 | 4.9 | rerank higher |
| shared practice: bm25 minus rerank_c10 | 20 | -0.193 | [-0.444, +0.065] | 5,936 | 3.0 | not distinguishable |
| shared practice: dense minus rerank_c10 | 20 | -0.138 | [-0.333, +0.058] | 5,936 | 3.0 | not distinguishable |
| shared practice: hybrid minus rerank_c10 | 20 | -0.229 | [-0.406, -0.059] | 5,936 | 3.0 | rerank_c10 higher |
| shared practice: rerank_c10 minus rerank | 20 | -0.100 | [-0.225, +0.000] | 3,280 | 1.9 | not distinguishable |
| own: bm25 minus rerank | 35 | -0.131 | [-0.236, -0.040] | 9,275 | 3.1 | rerank higher |
| own: dense minus rerank | 35 | -0.266 | [-0.405, -0.137] | 9,275 | 3.1 | rerank higher |
| own: hybrid minus rerank | 35 | -0.133 | [-0.240, -0.040] | 9,275 | 3.1 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_potion.jsonl | dense_potion | 35 | 0.09 | 2.6 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 35 | 0.06 | 1.8 |
| traces/retrieval/own-own-dense.jsonl | dense | 35 | 0.18 | 5.0 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 35 | 0.31 | 8.9 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.05 | 2.6 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.17 | 8.6 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.27 | 13.5 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.11 | 2.7 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.34 | 8.5 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.52 | 13.0 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Option 3, "Cost and Latency"

I made a copy of the reranker but changed it to see the top 10 candidates instead of the top 20. The files that hold it are rerank_c10.py, rerank_c10.practice.trec, and shared-practice-rerank_c10.jsonl

stretch-cost

The interval lets me claim that I am saving tokens per query (3280 per query) and time per query (1.9 seconds), and that the interval is [-0.225, 0], MRR@10 dropped from 0.800 to 0.700 which is not distinguishable. It just tells me that it is cheaper, I can't claim if it's worse or not. I can claim that even the cheaper rerank_c10 does better than hybrid, but isn't distinguishable for bm25 or dense. As of now, I would not make this trade because while it saves tokens, it doesn't make sense to drop so much and have it be not distinguishable anymore, but further testing would validate this. This would make sense in a situation where the cost and speed matter a lot, like a trivia game where finding the information quickly is more important than completely accurately, but you wouldn't want to use this where accuracy matters, like anything that is truly critical

In the future, I would want to run it on 15 candidates to figure out optimal amounts for cost saving but also more accurate answers. I also would want to run this with more queries to get a better baseline. I want the interval to not touch zero, which is when I would know if the drop is actually real.


---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
