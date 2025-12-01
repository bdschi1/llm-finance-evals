# Portfolio Risk Decomposition Notes

This document sketches the risk and attribution concepts that underpin how
this repo evaluates LLMs on portfolio reasoning tasks.

The high-level idea is to view a portfolio’s risk as coming from:

- **Systematic / factor risk** – exposure to broad drivers (market, sector, style factors).
- **Idiosyncratic risk** – name-specific risks tied to fundamentals, events, or execution.
- **Concentration and correlation structure** – how much risk is dominated by a few names,
  sectors, or factors, and how correlated those positions are.

For evaluation purposes, the questions are:

1. Can the model distinguish between **factor exposure** (e.g., “this portfolio is long quality
   and short small-cap value”) and **stock-specific bets**?
2. Does the model identify where risk is **concentrated** (e.g., single-name, sector, theme)?
3. When given a simple attribution or risk report, does the model reason about:
   - Whether the risk is **intentional or unintended**.
   - How changes in position sizing would change the risk profile.
4. Can the model propose **concrete adjustments** (e.g., trims, pairs, hedges) that reduce
   unintended risk while preserving the core thesis?

Future work in this repo will add eval tasks and golden answers that reflect this
decomposition, so that PMs and analysts can see whether LLMs reason about portfolios
in a way that aligns with how risk is actually managed in practice.
