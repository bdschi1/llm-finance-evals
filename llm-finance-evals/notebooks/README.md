
# notebooks

Runnable examples for the evaluation suite.

Current demo:

- `run_eval_demo.py` – command-line script that:
  - loads sample input data from `/data`,
  - uses the golden answers in `/golden_answers` as stand-ins for model outputs,
  - and scores them using the rubric functions in `/scoring`.

Usage (from the repo root):

```bash
python notebooks/run_eval_demo.py

---

At this point, your repo has:

- Structured eval configs (`/evals`).
- Real data and golden answers (`/data`, `/golden_answers`).
- A clear error taxonomy (`/error_taxonomy`).
- Scoring logic (`/scoring`).
- A runnable demo (`/notebooks/run_eval_demo.py`).


