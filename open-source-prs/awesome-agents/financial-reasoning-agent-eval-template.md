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

Score each dimension on a 1–5 scale:

1. **Factual Accuracy**
   - 1: Multiple material factual errors.  
   - 3: Mostly accurate; minor issues that don’t change the conclusion.  
   - 5: No material factual errors; grounded in the source.

2. **Understanding of Business Model & Drivers**
   - 1: Superficial; misses key revenue/cost drivers.  
   - 3: Understands main drivers; misses some nuance.  
   - 5: Clear and coherent understanding of how the company creates value.

3. **Risk Awareness (Idiosyncratic, Sector, Macro)**
   - 1: Ignores key risks a PM would immediately flag.  
   - 3: Identifies several important risks but misses some obvious ones.  
   - 5: Surfaces major idiosyncratic, sector, and macro risks; links them to thesis and sizing.

4. **Reasoning Quality & Internal Consistency**
   - 1: Contradictions, unclear logic, leaps of reasoning.  
   - 3: Mostly coherent; some gaps.  
   - 5: Step-by-step, explicit assumptions, clean causal logic.

5. **Actionability for PM/Analyst Workflows**
   - 1: Too vague to use in real decision-making.  
   - 3: Directionally helpful but incomplete.  
   - 5: Directly usable as a starting point for research or risk discussions.

6. **Hallucination Control / Source Grounding**
   - 1: Fabricates metrics, events, or facts.  
   - 3: Mostly grounded; occasional unsupported statements.  
   - 5: Clear separation of facts, estimates, and assumptions.

---

## 3. Example Task Specifications

Below are three standardized tasks suitable for PM/analyst evaluation.  
Replace tickers/portfolios with your own.

---

### Task A — Earnings Quality & Thesis Skeleton

**Prompt to agent:**  
> You are an equity analyst. Read the attached quarterly earnings materials  
> and buyside/sellside research for TICKER.  
> 1) Summarize the quarter in 10 bullet points.  
> 2) Identify 5 key drivers of forward EPS/FCF.  
> 3) Propose a preliminary long/short view and list 5 thesis-breaking risks.  
> 4) State explicitly what additional data you need.

**Evaluator notes:**  
- Focus on whether the agent captures essence, not prose quality.  
- High score = risk-aware, non-naive, PM-grade takeaways.

---

### Task B — Portfolio Risk & Exposure Sanity Check

**Prompt to agent:**  
> You are a PM. Using the attached portfolio snapshot (weights, sectors, factor betas):  
> 1) Identify the top 3 concentration risks.  
> 2) Describe the portfolio’s main factor exposures.  
> 3) Suggest 3 adjustments to reduce unintended risk without breaking the thesis.

**Evaluator notes:**  
- Penalize generic “risk is high” statements.  
- High score = portfolio-specific, PM-relevant reasoning.

---

### Task C — Risk Disclosure & Landmine Detection

**Prompt to agent:**  
> Read the Risk Factors section of the attached 10-K and the relevant  
> buyside/sellside research for TICKER.  
> 1) List 10 risks relevant to a long investor.  
> 2) List 10 risks relevant to a short seller.  
> 3) Highlight 3 “sleep-at-night” issues (major drawdown risks).

**Evaluator notes:**  
- High score requires distinguishing boilerplate vs real, material risks.

---

## 4. Scoring & Aggregation

For each task:

- Score all dimensions from 1–5.  
- Compute:  
  - **Overall Score** = average of all dimensions.  
  - **Decision-Usefulness Score** = average of Understanding + Risk Awareness + Actionability.

Maintain logs (CSV/JSON) containing:

- Model/agent name and version  
- Task ID  
- Scores per dimension  
- Notes on failure modes and dangerous behavior

---

## 5. Usage

Use this template to:

- Compare multiple agents and model versions.  
- Track performance changes as prompts or tools evolve.  
- Document evaluation standards for PMs, analysts, ML teams, and leadership.

The emphasis is *professional investment workflows*, not generic QA.
