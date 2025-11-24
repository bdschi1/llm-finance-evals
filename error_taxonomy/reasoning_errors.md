# Reasoning errors in equity research and risk tasks

This document describes common **reasoning errors** that LLMs (and humans) make when performing equity research, risk, and portfolio-level tasks. These categories are used when reviewing model outputs and assigning scores in the evals.

---

## 1. Inconsistent thesis logic

- The stated thesis and the supporting arguments do not line up.
- Example: The model claims the stock is a long because growth will accelerate, but most of the argument discusses shrinking end markets and loss of share.

**Why it matters:** Inconsistent logic is hard to act on and is a red flag for decision quality.

---

## 2. Missing or weak link between drivers and outcome

- The model mentions drivers (e.g., volume growth, pricing, new product) but never explains *how* or *why* they lead to revenue, margin, or multiple changes.
- Example: “New product launch will drive upside” with no discussion of uptake, pricing, or competitive response.

**Why it matters:** Good theses and risk notes must connect drivers to P&L, not just list headlines.

---

## 3. One-sided analysis (no consideration of risks or alternatives)

- The output reads like a marketing pitch: only upside (for longs) or only downside (for shorts) with no acknowledgment of what could go wrong.
- Example: A long thesis with no mention of execution risk, competition, or macro sensitivity.

**Why it matters:** Real investment decisions require explicit consideration of what could invalidate the thesis.

---

## 4. Over-generalization and boilerplate

- The model produces generic statements that could apply to almost any company or sector.
- Example: “Management execution is a key risk and macro uncertainty may impact results” with no company-specific detail.

**Why it matters:** Boilerplate language hides whether the model understands the specific situation.

---

## 5. Time-horizon confusion

- Mixing short-term and long-term views without being explicit, or contradicting the stated investment horizon.
- Example: Calling out a one-quarter earnings miss as thesis-breaking in a 3-year secular growth thesis.

**Why it matters:** Risk and sizing decisions depend heavily on aligning the reasoning with the intended horizon.

---

## 6. Misuse of factor or exposure information

- The model references style/sector/country exposures but draws incorrect conclusions.
- Example: Calling a position “defensive” despite clear exposure to high-beta growth factors.

**Why it matters:** Misreading exposures leads to bad portfolio construction and risk aggregation.

---

## 7. Poor structure and prioritization

- The right ideas may be present, but they are buried, disorganized, or not prioritized.
- Example: Mixing key thesis points, edge, and minor risks in a single long paragraph.

**Why it matters:** PMs and risk committees need to skim quickly and still understand the main points.
