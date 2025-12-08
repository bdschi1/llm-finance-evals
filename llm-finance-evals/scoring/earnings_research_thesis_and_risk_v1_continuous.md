# Continuous / Dynamic Scoring: Earnings Research Thesis and Risk (v1)

This file extends the discrete 1–5 rubric for
`earnings_research_thesis_and_risk_v1` with a **continuous and dynamic
scoring scheme** that can evolve as new information is introduced and the
model revises its answer.

The goal is to:

- Track **continuous scores** in [0, 1] (or 0–100) instead of only 1–5
  buckets, and
- Allow scores and conviction to **update over iterations** as new data,
  price moves, or portfolio context are provided.

This rubric does not replace the discrete rubric; it is an optional,
more granular layer for experiments.

---

## 1. State Representation

For each model run, maintain a scoring state:

- Per-dimension continuous scores:
  - `factual_grounding_score`   ∈ [0, 1]
  - `driver_understanding_score` ∈ [0, 1]
  - `risk_awareness_score`      ∈ [0, 1]
  - `conviction_event_path_score` ∈ [0, 1]
  - `positioning_risk_use_score`  ∈ [0, 1]
  - `clarity_structure_score`     ∈ [0, 1]

- A **composite score**:
  - `overall_score` ∈ [0, 1] (e.g., a weighted average of dimensions).

- A **conviction state**:
  - `thesis_conviction` ∈ [0, 1] (probability-like),
  - `sizing_conviction` ∈ [0, 1] (how confident the sizing / risk usage is).

---

## 2. Initialization (Iteration 0)

On the initial answer (before any new information):

1. Score the output using the discrete 1–5 rubric.
2. Map discrete to continuous using a simple linear mapping, e.g.:

   - 1 → 0.10  
   - 2 → 0.30  
   - 3 → 0.50  
   - 4 → 0.70  
   - 5 → 0.90  

3. Initialize:

   - Each per-dimension score from the mapped value,
   - `overall_score` as a weighted average,
   - `thesis_conviction` and `sizing_conviction` from the
     **Conviction Levers & Event Path** and **Positioning & Risk Use**
     dimensions (e.g., their average).

This gives a continuous baseline state that corresponds to the discrete
rubric but is more granular.

---

## 3. Updating Scores with New Information

When new information is provided (e.g., an earnings print, new guidance,
price move, or risk/attribution report), the model produces an **updated
answer** and the evaluator updates the scores.

For each dimension, define:

- `old_score` – the current continuous score in [0, 1].
- `signal_score` – a provisional score in [0, 1] based on the updated
  answer alone (i.e., “if I scored this iteration from scratch”).
- `alpha` – an update rate in [0, 1] (e.g., 0.3–0.5) representing how
  quickly scores respond to new information.

Update rule (simple exponential smoothing):

new_score = (1 - alpha) * old_score + alpha * signal_score

#If alpha is high (0.7–0.9), scores move quickly with new data.

#If alpha is low (0.1–0.3), scores change slowly and require more
consistent evidence.
