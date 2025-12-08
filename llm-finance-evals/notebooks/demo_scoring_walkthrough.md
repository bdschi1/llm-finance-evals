# Demo: Scoring an LLM Long/Short PM Response

This notebook walks through:

1. Selecting a scenario  
2. Running a model (or pasting its output) as Long PM or Short PM  
3. Loading the scoring schema and rubric  
4. Producing a component-level score  

---

## Step 1 — Choose scenario

Example:
`ai_infra_vs_productivity_rotation_event_path`

## Step 2 — Generate model output

You can paste a model output into:
`example_model_output.txt`

And the matching golden answer (for comparison) into:
`example_golden_answer.txt`

## Step 3 — Run scoring

```bash
python scoring/score_output.py
