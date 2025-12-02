# Portfolio Risk Decomposition Notes

These notes sketch the risk and attribution concepts behind the evals in
this repo.

Working assumptions:

- In a long/short equity book, **risk is the budgeting currency**.
  Positions are sized in units of risk, not just dollars or notional.
- Every position consumes a slice of a finite risk budget, decomposed into:
  - **Systematic / factor risk** (market, sector, style),
  - **Idiosyncratic risk** (stock-specific),
  - **Convexity / tail risk** (options, gap risk, binary events).
- The portfolio should be decomposed into additive risk slices
  (factors, sectors, styles, single names, legs of pairs, tail scenarios),
  where each slice has:
  - An explicit role (alpha source, hedge, structural exposure),
  - A capped contribution to total volatility and drawdown.

For eval design, the key questions are:

1. Can a model distinguish factor vs idiosyncratic risk and explain how a
   position changes the risk profile of a book?
2. Does it identify where risk is concentrated (single-name, sector, theme,
   factor, event path)?
3. When given a small risk/attribution report, can it reason about:
   - Which risks are intentional vs accidental?
   - How to resize or rebalance to improve **alpha per unit of marginal risk**?
4. Can it propose concrete trades (trims, pairs, hedges) that align the
   portfolio with a stated risk budget?

Future eval tasks will map these concepts into prompts, golden answers, and
scoring rubrics so that model behavior can be judged the way a PM or risk
manager would judge a book review.
