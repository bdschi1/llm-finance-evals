# Evaluation Template for Financial-Reasoning AI Agents

This template provides a structured way to evaluate AI agents that perform
financial analysis, portfolio reasoning, and investment research tasks.
It is intended for use by portfolio managers, analysts, and ML practitioners
who need consistent, PM-grade evaluation of agent behavior.

---

## 1. Scope and Use Cases

Use this template when an AI agent is asked to:

- Analyze earnings reports (10-K, 10-Q, 20-F, investor presentations) and buyside/sellside research.
- Propose or critique a long/short equity thesis.
- Assess portfolio-level risk/exposures, including factor and sector risks.
- Summarize key business or regulatory risks relevant to an investment decision.

The template does **not** assume a single “right answer.” Instead, it focuses
on whether the agent’s output is *decision-useful* and *risk-aware* for
professional portfolio managers and analysts.

---

## 2. Core Evaluation Dimensions

Each response should be scored from 1–5 on the following dimensions:

1. **Factual Accuracy**
   - 1: Multiple material factual errors.
   - 3: Mostly accurate; minor issues that do not change the conclusion.
   - 5: No material factual errors; citations or clear grounding in the source.

2. **Understanding of Business Model & Drivers**
   - 1: Superficial description; misses key revenue/cost drivers.
   - 3: Correct core drivers but misses second-order dynamics.
   - 5: Clear, coherent description of how the company makes and loses money.

3. **Risk Awareness (Company-Specific and Structural)**
   - 1: Ignores or trivializes key risks that a human PM would flag immediately.
   - 3: Identifies several important risks but misses some obvious ones.
   - 5: Surfaces major idiosyncratic, sector, and macro/structural risks, and
        links them to the thesis and position sizing.

4. **Reasoning Quality and Internal Consistency**
   - 1: Contradictions, unstructured narrative, or unexplained jumps in logic.
   - 3: Mostly coherent but with some gaps or hand-waving.
   - 5: Step-by-step reasoning, explicit assumptions, and clear “because → therefore” logic.

5. **Actionability for a PM/Analyst**
   - 1: Vague commentary; cannot inform a position or risk decision.
   - 3: Directionally helpful but would require significant human rework.
   - 5: Directly usable as a starting point for a research note, risk memo, or PM discussion.

6. **Hallucination Control / Use of Sources**
   - 1: Fabricates figures, events, or citations.
   - 3: Mostly grounded but with some unsupported claims.
   - 5: Clearly distinguishes between known facts, estimates, and assumptions.

---

## 3. Example Task Specifications

Below are three standardized tasks. Replace the ticker/portfolio with your own.

### Task A – Earnings Quality and Thesis Skeleton

**Prompt (to the agent)**  
> You are an equity analyst. Read the attached Q3 earnings materials and relevant  
> buyside/sellside research for TICKER.  
> 1) Summarize the quarter in 10 bullet points.  
> 2) Identify the 5 most important drivers of forward EPS and FCF.  
> 3) Propose a preliminary long/short view and list 5 key risks that could break the thesis.  
> 4) Explicitly state what data you would need next to refine the view.

**Evaluator notes:**  
- Focus on whether the agent captures the *essence* of the quarter, not prose quality.  
- High scores require risk-aware, non-naïve commentary (no “everything is fine” summaries).

---

### Task B – Portfolio Risk & Exposure Sanity Check

**Prompt (to the agent)**  
> You are a portfolio manager. Given the attached portfolio snapshot (names, weights,  
> sectors, regions, and factor betas), perform a risk sanity check:  
> 1) Identify the top 3 concentration risks.  
> 2) Describe the portfolio’s main factor exposures.  
> 3) Suggest 3 concrete ways to reduce unintended risk without destroying the core thesis.

**Evaluator notes:**  
- High scores if the agent can explain risk in language that a PM or CIO would find credible.  
- Penalize vague or generic risk advice that ignores the specific portfolio.

---

### Task C – Risk Disclosure and Landmine Detection

**Prompt (to the agent)**  
> Read the Risk Factors section of the attached 10-K for TICKER and any relevant  
> buyside/sellside research.  
> 1) List 10 risks that are most relevant to a long-only investor.  
> 2) List 10 risks that are especially relevant to a short seller.  
> 3) Highlight 3 “sleep-at-night” issues for a PM (things that could cause a major drawdown).

**Evaluator notes:**  
- High scores require differentiation between generic/legal boilerplate and real, material risks.

---

## 4. Scoring and Aggregation

For each task:

- Score each dimension from 1–5.
- Compute:
  - **Overall Score** = average of all dimensions.
  - **Decision-Usefulness Score** = average of (Understanding, Risk Awareness, Actionability).

Keep a simple log (CSV/JSON) with:
- Model/agent name and version
- Task ID (A, B, C…)
- Scores per dimension
- Notes on failure modes

---

## 5. Usage

You can use this template to:

- Compare multiple agents or model versions on the same financial tasks.
- Track progress over time as prompts, tools, or models change.
- Communicate evaluation results to portfolio managers, analysts, data scientists,
  and leadership in a structured way.

Feel free to adapt the specific tasks or scoring scale, but keep the focus on
decision-usefulness and risk-awareness in professional investment workflows.
