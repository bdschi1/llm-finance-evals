# llm-finance-evals

Domain-specific evals for LLMs on equity research, risk, and portfolio reasoning, with golden answers, error taxonomies, and scoring tools.

---

## Overview

This repository provides a practical evaluation suite for large language models (LLMs) on real-world investment tasks: equity research, risk assessment, and portfolio-level reasoning.

The goal is not just to see if a model is “smart,” but to measure whether it behaves like a competent analyst or PM on tasks that matter for P&L and risk.

This repo is designed so that:

- **Engineers / ML teams** can plug in different models and run reproducible, scriptable evals.
- **Executives / PMs / risk** can see clearly what is being tested, how it is scored, and where the model is safe vs unsafe to deploy.

---

## What’s in this repo?

The project is organized around four core components:

- **Evals (`/evals`)**  
  Structured definitions and configs for domain-specific evaluation tasks (e.g., thesis quality, risk notes, scenario analysis).

- **Golden answers (`/golden_answers`)**  
  Canonical, human-written responses that represent “good” output by investment standards.

- **Error taxonomy (`/error_taxonomy`)**  
  A catalog of common model failure modes in equity research and risk (e.g., hallucinated fundamentals, flawed risk logic, missing drivers).

- **Scoring tools (`/scoring`)**  
  Simple scripts and rubrics that turn model outputs into transparent scores and rationales.

### Scoring frameworks

Scoring is intentionally layered so you can start simple and add structure:

- **Discrete rubric (baseline)**  
  Per-task, 1–5 scores on dimensions such as factual grounding, driver understanding, risk awareness, conviction levers / event path, and positioning & risk use.

- **Continuous / dynamic scoring (optional)**  
  Continuous scores in `[0, 1]` that update as new information is provided and the model revises its answer. Designed to capture conviction trajectories over an event path instead of one-shot answers.

- **Bayesian scoring (optional)**  
  Treats conviction as a probabilistic belief that a thesis is economically “right” and that sizing is appropriate. Uses simple Bayesian updates (e.g., Beta/Bernoulli) to move from prior to posterior beliefs as events unfold, then maps posterior conviction to position size in risk units.

- **Conviction slugging (experimental)**  
  Measures payoff power per unit of risk when the model “swings” its risk budget: the ratio of realized or simulated P&L per risk unit on higher-conviction sizing decisions, analogous to slugging percentage in baseball.

- **Planned expansions (future)**  
  Planned future work includes more explicit portfolio-risk and attribution evals based on factor vs idiosyncratic risk decomposition, so that models are tested on the same logic used in real portfolio construction and risk reviews.

Supporting these, there are:

- **Notebooks / scripts (`/notebooks`)**  
  Runnable examples (e.g., `demo_scoring_walkthrough.md`) and simple CLI usage via `scoring/score_output.py` that show end-to-end scoring.

- **Data (`/data`)**  
  Synthetic or public input snippets (no confidential data), including scenario descriptions and event paths.

- **Docs (`/docs`)**  
  Additional workflow explanations, review examples, and design notes (to be expanded).

- **Results (`/results`)**  
  Placeholder directory for scored outputs and logs produced by evaluation runs.

---

## Intended audience

This repo is aimed at:

- **AI / ML / platform teams** at funds, banks, and fintechs who need concrete, finance-specific evals rather than generic benchmarks.  
- **Domain-expert AI trainer / evaluator roles** who design tasks, datasets, and rubrics for LLM-based research tooling.  
- **PMs, research heads, and risk managers** who want to understand how LLM performance is being measured before relying on it in live workflows.

---

## Author and context

These evals are based on my experience as a **long/short healthcare portfolio manager and research lead**, building and running fundamental and factor-aware equity strategies across multi-manager and owner-operated funds.

The focus here is on tasks that actually show up in live workflows, including:

- Pre- and post-earnings work  
- Biotech/clinical and regulatory risk  
- Portfolio and factor exposure reviews  
- Scenario analysis for event-driven positions  

The goal is to make it easy for AI/ML teams to plug in models, while PMs, research heads, and risk can see clearly how model behavior maps to decision quality and P&L.

---

## How to Run an Evaluation

This repository includes a complete end-to-end evaluation pipeline for assessing
LLM reasoning quality in long/short equity portfolio management tasks.

Follow the steps below to run a basic evaluation.

### 1. Select a scenario

Scenarios live in:

```text
data/scenarios/

Example: ai_infra_vs_productivity_rotation_event_path
