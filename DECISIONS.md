# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

This is answered after in the git history because I quit it without saving :( 

I chose the corpus because I am an avid video game enjoyer! I know a lot of Pokemon, but could always learn more and am always trying to understand the lore of different games, so I wanted to be able to see all of the different ways the games interact together and answer similar questions. It is just a great way for me to learn more and test my own trivia to see how the games interact together. 

From my memory, my answer was that I thought that hybrid would do the best because it is able to understand and match the actual wording via bm25, but also put it together using natural language in dense. It makes the most sense that this would do the best because it finds key words and then is able to make human sense of them. I think that bm25 would do the worst because it is just focusing on the words and word matching, and Pokemon is so verbose and a lot of the characters and pokemon are similar, so it is easy to get tangled up in words very quickly.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

TODO: your answer to prompt 2.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

The real instance of me going against the AI was during c08, where Claude had flagged one of the candidates I didn't mark and asked whether or not I thought it was relevant, leaning towards it was relevant and should be counted. I looked at the snippet and decided it didn't matter originally, but after looking at the failure analysis of the query, I decided that Claude had been correct and I had to rescore with the correct candidate. I noticed this because it was a failing query, but looking through the candidates I had felt that it should have been scored differently. This mattered because it made bm25 vs dense not distinguishable. 

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

TODO: your answer to prompt 4.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

I think that my gold set needs to be worked on, the articles are verbose and might answer part of the question or more of the question that I originally marked down, so I think that the gold set needs to be more tailored with better information, and there has to be some way for me to figure out what to do if part of the question is answered but not all of it, like charmander evolving into charmeleon, then into charizard, rather than the direct answer I was looking for. I would likely use graded labels to fix this in the future. This happened in query h02 with the labels in qrels.txt. Finally, to see if this matters I would relabel queries with the graded labels and compare the scoring with both graded and not graded labels of the same queries. 