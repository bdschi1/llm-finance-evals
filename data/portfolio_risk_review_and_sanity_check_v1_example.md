# Example Input: Portfolio Risk Review and Sanity Check (v1)

This is a synthetic example of the input package for the eval
`portfolio_risk_review_and_sanity_check_v1`.

A full implementation would provide a **simple but structured snapshot** of
a long/short equity book, including:

- **Top positions** (longs and shorts) with:
  - Ticker / name,
  - Position size in risk units,
  - Sector / industry,
  - Basic thesis tags (growth, value, event-driven, etc.).

- **Risk decomposition summary**:
  - Portfolio volatility and VaR-like metrics,
  - Contributions from:
    - Market / beta,
    - Sectors or industries,
    - Style factors (value, growth, quality, momentum, size),
    - Idiosyncratic risk.

- **Concentration and crowding indicators** (synthetic):
  - Largest single-name risk contributors,
  - Theme or sector clusters,
  - Flags for overlapping exposures.

- **Scenario or stress test results**:
  - Example macro or thematic shocks (e.g., rates up, growth selloff),
  - Approximate P&L impact by sector/theme and by top positions.

In this v1, the focus is on defining the **structure** of the eval rather
than providing real portfolio data. Concrete numbers and a toy book can be
added later without changing the schema.
