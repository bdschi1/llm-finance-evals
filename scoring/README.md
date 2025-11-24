# scoring

Simple, rubric-based scoring scripts for the evals in this repository.

Current modules:

- `equity_research_rubric.py` – scores equity research theses according to the
  dimensions and weights defined in `evals/equity_research_eval.yaml`.
- `risk_logic_rubric.py` – scores risk summaries according to the
  dimensions and weights defined in `evals/risk_logic_eval.yaml`.

At this stage, both modules implement neutral stub scoring (default score 3.0
on a 1–5 scale) and return a structured result that can be consumed by:

- human reviewers (who can overwrite scores and add notes), or
- future automated judging logic (heuristics or LLM-as-judge).

The intent is to make the scoring logic transparent and easy to extend, not to
fully automate judgment on day one.
