# Hallucination patterns in equity and risk outputs

This document focuses on **hallucinations** – confident statements that are not supported by the prompt or reasonable domain knowledge in the given context.

---

## 1. Invented events or news

- The model describes earnings, regulatory decisions, M&A, or clinical trial outcomes that are **not mentioned** in the input.
- Example: Claiming the FDA has already approved a new indication when the prompt only says "filing submitted".

**Risk:** Directly misleads decision-makers and can contaminate downstream notes and models.

---

## 2. Fabricated quantitative metrics

- Creating specific numbers (growth rates, margins, EPS, valuation multiples) that are not in the prompt.
- Example: Stating “EBIT margin expanded from 15% to 20%” when no such numbers are provided.

**Risk:** These numbers may be copied into spreadsheets or decks without verification.

---

## 3. False consensus or market view statements

- Asserting what “the market expects” or “consensus assumes” with no given data.
- Example: “Consensus is too optimistic on margin expansion” without any reference to estimates or guidance in the prompt.

**Risk:** Encourages users to anchor on an invented view of positioning and expectations.

---

## 4. Confident but unsupported sector or policy claims

- Making strong claims about regulation, reimbursement, or clinical standards that do not follow from the input.
- Example: “Recent legislation guarantees higher hospital reimbursement” with no such detail in the context.

**Risk:** Policy and regulatory misunderstandings can lead to large, asymmetric losses.

---

## 5. Overstated certainty

- Presenting speculative inferences as hard facts.
- Example: “Management will definitely miss guidance” based on limited qualitative hints.

**Risk:** Distorts risk perception; can push users toward overconfident sizing or timing decisions.

---

## 6. Spurious name or ticker substitutions

- Swapping in a different company name or ticker mid-answer, or mixing facts from multiple companies.
- Example: Starting with ACME MedTech and then suddenly referring to another medtech name without any prompt support.

**Risk:** Confuses attribution and can lead to misaligned trades or notes.

---

## 7. Synthetic source citations

- Referring to non-existent reports, filings, or data sources.
- Example: “As shown in the latest 10-K, page 42…” when no such document was provided.

**Risk:** Undermines trust in the entire workflow and makes it harder to audit outputs.

---

## Handling hallucinations in evals

When reviewing outputs for evals in this repo:

- **Flag** hallucinations explicitly in review notes.
- **Down-score** outputs where hallucinations affect the thesis, risk view, or recommended action.
- **Document** recurring patterns so scoring scripts and prompts can be adjusted over time.
