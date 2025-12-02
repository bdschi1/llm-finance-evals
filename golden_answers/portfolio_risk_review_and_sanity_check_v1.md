# Golden Answer: Portfolio Risk Review and Sanity Check (v1)

This file sketches the structure and key elements of a **PM-quality risk
review** for the eval `portfolio_risk_review_and_sanity_check_v1`.

## 1. High-Level Portfolio Summary

- 2–3 paragraphs summarizing:
  - Overall book construction (net, gross, typical position sizes),
  - Main themes / sectors / styles,
  - Any obvious skew (e.g., growth vs value, cyclicals vs defensives).

The goal is to show that the model can read the snapshot and articulate
what kind of book this is.

## 2. Risk Decomposition

- Clear description of how total risk is split across:
  - Market / beta exposure,
  - Sectors and industries,
  - Style factors,
  - Idiosyncratic single-name risk,
  - Any tail/convexity exposures (if present).

- Short commentary on:
  - Which components are **intentional** (aligned with stated themes),
  - Which look like **residual / accidental** bets.

## 3. Intentional vs Accidental Risks

- Explicit list of **intended risks** (e.g., long quality growth vs value,
  short specific sectors, long/short within a theme).
- Explicit list of **accidental or undesired risks**, such as:
  - Net beta that is higher or lower than intended,
  - Sector tilts that are larger than justified by conviction,
  - Style tilts (e.g., unintended small-cap or momentum bias),
  - Over-reliance on a single macro driver (like rates or FX).

For each accidental risk, a short explanation of “why this is a problem.”

## 4. Concentration and Crowding Checks

- Identification of:
  - Top single-name contributors to risk and to potential drawdown,
  - Theme/sector clusters that dominate risk,
  - Any signs that the book is effectively one big trade in disguise.

- Commentary on:
  - Whether concentration is justified by conviction and slugging potential,
  - How crowding or overlap could amplify drawdowns.

## 5. Actionable Changes (Rebalance Plan)

- Concrete recommendations, such as:
  - **Trims** to reduce unintended exposures,
  - **Adds** to increase underweight but high-conviction areas,
  - **Pairs** to neutralize factor risks while preserving alpha views,
  - **Hedges** (index, sector, thematic) for macro or tail risks.

Each recommendation should link back to:

- A specific risk or concentration issue identified above,
- The impact on the risk budget (e.g., “reduces sector X risk contribution
  from 18% to ~12% of total,” “brings net beta back toward target”).

## 6. Risk-Budget and Scenario Commentary

- A short discussion of:
  - How the current book consumes the finite risk budget across factors,
    sectors, themes, and idiosyncratic names.
  - Whether the risk budget is being used where expected **alpha per unit
    of marginal risk** is highest.

- Scenario commentary:
  - How the book behaves under a small set of defined scenarios (e.g., growth
    selloff, rate shock, sector-specific drawdown),
  - Whether the book’s response to these scenarios matches the PM’s stated
    intentions.

This golden answer is a **reference pattern**. Model outputs are scored on
how closely they match this structure, depth of risk reasoning, and the
quality of **actionable portfolio changes**, not on any specific numbers.
