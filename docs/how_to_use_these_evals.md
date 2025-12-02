# How to Use These Evals

This repo provides **domain-specific evaluation units** for large language
models and agents on equity research, risk, and portfolio reasoning.

It is designed for two main audiences:

- **Engineers / platform / ML teams** who want structured, scriptable evals.
- **PMs / analysts / domain-evaluator roles** who want to judge whether
  models think and behave like a competent long/short PM, not just
  “sound smart.”

This document explains how to use the evals in both **manual** (by hand)
and **programmatic** (via scripts/agents) workflows.

---

## 1. Eval Units in This Repo

Each eval unit has the same basic structure:

- An **eval definition** in `evals/`  
- An **input package** (or stub) in `data/`  
- A **golden answer pattern** in `golden_answers/`  
- One or more **scoring frameworks** in `scoring/`

### 1.1 Earnings Research: Thesis and Risk (v1)

- Definition:  
  `evals/earnings_research_thesis_and_risk_v1.json`

- Input stub:  
  `data/earnings_research_thesis_and_risk_v1_example.md`

- Golden answer pattern:  
  `golden_answers/earnings_research_thesis_and_risk_v1.md`

- Scoring:
  - Discrete rubric:  
    `scoring/earnings_research_thesis_and_risk_v1.md`
  - Continuous / dynamic (optional):  
    `scoring/earnings_research_thesis_and_risk_v1_continuous.md`
  - Bayesian conviction (optional):  
    `scoring/earnings_research_thesis_and_risk_v1_bayesian.md`
  - Conviction Slugging (cross-cutting experiment):  
    `scoring/conviction_slugging_experiment.md`

**What it tests**

Whether a model can:

- Read an earnings / company input packet (filings + commentary + buyside/sellside-style summary).
- Produce a **PM-grade** long or short thesis.
- Identify **drivers and KPIs**, **risks**, **event path and conviction levers**.
- Propose **sizing and role in a long/short portfolio** in **risk units**.

---

### 1.2 Portfolio Risk Review and Sanity Check (v1)

- Definition:  
  `evals/portfolio_risk_review_and_sanity_check_v1.json`

- Input stub:  
  `data/portfolio_risk_review_and_sanity_check_v1_example.md`

- Golden answer pattern:  
  `golden_answers/portfolio_risk_review_and_sanity_check_v1.md`

- Scoring:
  - Discrete rubric:  
    `scoring/portfolio_risk_review_and_sanity_check_v1.md`
  - Conviction Slugging (if event-path + sizing changes are simulated):  
    `scoring/conviction_slugging_experiment.md`
  - Bayesian / continuous concepts can be reused but are not wired to this
    eval yet.

**What it tests**

Whether a model can:

- Read a **portfolio snapshot** with longs/shorts, risk decomposition, and scenarios.
- Distinguish **intentional vs accidental risks**.
- Diagnose **concentration, crowding, and overlap**.
- Propose **actionable portfolio changes** (trims/adds/pairs/hedges) framed in **risk units and risk budget** terms.

---

## 2. Manual Workflow (PM / Domain-Evaluator)

This is how a PM, analyst, or AI trainer could use the evals **by hand**.

### 2.1 Earnings eval: manual use

1. Open the eval definition:
   - `evals/earnings_research_thesis_and_risk_v1.json`
   - Note the expected output sections.

2. Open the input example:
   - `data/earnings_research_thesis_and_risk_v1_example.md`
   - Treat this as the “packet” you would hand to a model (or junior analyst).

3. Prompt a model (or human analyst) using your interface of choice:
   - Paste the input packet.
   - Ask them to respond in the structure defined in the JSON and
     golden answer pattern.

4. Compare the output against:
   - Golden answer pattern:  
     `golden_answers/earnings_research_thesis_and_risk_v1.md`

5. Score using the discrete rubric:
   - `scoring/earnings_research_thesis_and_risk_v1.md`
   - For each dimension (factual grounding, risk awareness, etc.), assign a
     1–5 score and keep short notes on strengths/weaknesses.

6. Optional: annotate failure modes
   - Where did the model miss driver logic?
   - Where did it ignore risk budget / sizing?
   - Where did it hallucinate vs the input packet?

This is the **baseline human-evaluator loop**: it requires no code, just
files and a scoring rubric.

---

### 2.2 Portfolio risk eval: manual use

1. Open:
   - `evals/portfolio_risk_review_and_sanity_check_v1.json`
   - `data/portfolio_risk_review_and_sanity_check_v1_example.md`

2. Prompt a model with the portfolio snapshot:
   - Ask for a risk review in the structure defined in the JSON and
     golden answer.

3. Compare the output against:
   - `golden_answers/portfolio_risk_review_and_sanity_check_v1.md`

4. Score using:
   - `scoring/portfolio_risk_review_and_sanity_check_v1.md`

Focus on:

- Whether the model distinguishes **intentional vs accidental risk**.
- Whether it identifies **concentration, crowding, and structural bets**.
- Whether its rebalance suggestions are **specific, actionable, and aligned
  with a finite risk budget**.

---

## 3. Programmatic Workflow (Engineers / Platform)

You can also use these evals in a **scripted** pipeline.

### 3.1 High-level pattern

For each eval:

1. **Load the eval definition (JSON)**  
   - Parse `id`, `description`, `inputs`, `expected_outputs`, `scoring`.

2. **Load the input package (Markdown)**  
   - Read the `data/..._example.md` file indicated by the JSON.

3. **Build a prompt to the model or agent**  
   - System / instructions: summarise the task and expected sections.  
   - User content: the input package.

4. **Call the model / agent**  
   - Capture the response (JSON or text).

5. **Score the output**  
   - Discrete rubric: parse sections and apply the 1–5 rules in the
     relevant `scoring/*.md` file.
   - Optional: log continuous/Bayesian/slugging metrics if you implement
     those layers.

6. **Log results**  
   - Per-dimension scores,
   - Overall score,
   - Any derived metrics (Bayesian posterior, Conviction Slugging, etc.).

### 3.2 Example pseudo-code (earnings eval)

This is deliberately implementation-agnostic:

```text
load eval_def from "evals/earnings_research_thesis_and_risk_v1.json"
load input_md from eval_def.inputs.company_profile_and_docs

prompt = build_prompt(
  task_description = eval_def.description,
  expected_sections = eval_def.expected_outputs.sections,
  input_packet = input_md
)

model_output = call_model(prompt)

scores = score_output_discrete(
  output = model_output,
  rubric = "scoring/earnings_research_thesis_and_risk_v1.md"
)

# Optional extensions:
continuous_state = update_continuous_scores(scores, previous_state)
bayesian_state   = update_bayesian_beliefs(events, previous_bayesian_state)
slugging_metrics = compute_conviction_slugging(swings, pnl_per_risk)
