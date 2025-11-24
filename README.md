# llm-finance-evals

Domain-specific evals for LLMs on equity research, risk, and portfolio reasoning, with golden answers, error taxonomies, and simple scoring tools.

## Overview

This repository provides a practical evaluation suite for large language models (LLMs) on real-world investment tasks: equity research, risk assessment, and portfolio-level reasoning.  

The goal is not just to see if a model is “smart,” but to measure whether it behaves like a competent analyst/PM on tasks that matter for P&L and risk.

This repo is designed so that:

- **Engineers** can plug in different models and run reproducible evals.
- **Executives / PMs / risk** can see clearly what is being tested, how it is scored, and where the model is safe vs unsafe to deploy.

---

## What’s in this repo?

The project is organized around four core components:

- **Evals (`/evals`)**  
  Structured definitions of domain-specific evaluation tasks (e.g., thesis quality, risk notes, scenario analysis).

- **Golden answers (`/golden_answers`)**  
  Canonical, human-written responses that represent “good” output by investment standards.

- **Error taxonomy (`/error_taxonomy`)**  
  A clear catalog of common model failure modes in equity research and risk (e.g., hallucinated fundamentals, bad risk logic, missing drivers).

- **Scoring tools (`/scoring`)**  
  Simple scripts and rubrics that turn model outputs into transparent scores and rationales.

Supporting these, there are:

- **Notebooks (`/notebooks`)** with runnable examples and scorecards.
- **Data (`/data`)** with synthetic or public input snippets (no confidential data).
- **Docs (`/docs`)** for additional workflow explanations and diagrams.

---

## Intended audience

This repo is aimed at:

- **AI / ML / platform teams** at funds, banks, and fintechs who need concrete, finance-specific evals rather than generic benchmarks.
- **Domain-expert AI trainer / evaluator roles** who design tasks, datasets, and rubrics for LLM-based research tooling.
- **PMs, research heads, and risk** who want to understand how LLM performance is being measured before relying on it in live workflows.

---

## Folder structure

```text
llm-finance-evals/
  evals/            # Evaluation definitions and config files
  golden_answers/   # Canonical “golden” responses
  error_taxonomy/   # Failure-mode definitions and examples
  scoring/          # Scoring and rubric logic
  notebooks/        # End-to-end runnable examples
  data/             # Synthetic / public test inputs (no MNPI)
  docs/             # Additional documentation and diagrams
