# Conviction Slugging Experiment (Earnings Research & Event-Path Evals)

This file defines an experimental **Conviction Slugging** metric to evaluate
how well a model uses risk along an event path, in addition to the usual
rubrics.

## 1. Slugging Concept (Portfolio Definition)

In a long/short hedge fund, “slugging percentage” is the payoff power of the
book: how big your winners are relative to your losers, typically measured as
the ratio of average profit on winning positions to average loss on losing
positions (or more generally, P&L per unit of risk when you “swing”).

We adapt this notion to the evaluation setting by focusing on:

- **Swings in risk units** (changes in position size along the event path),
- The **realized or ground-truth P&L per unit of risk** associated with those
  swings, and
- The ratio of payoff power on good swings vs pain on bad swings.

---

## 2. Setup: Event Path and Swings

Given a scenario with an event path
\( t = 1, \dots, T \) (earnings, guidance, flow/positioning updates, etc.):

- Let \( R_{t-1} \) = risk units allocated to the idea before event \( t \).
- Let \( R_t \)   = risk units allocated after event \( t \).

Define the **swing size** at event \( t \):

\[
S_t = |R_t - R_{t-1}|
\]

If \( S_t = 0 \), the PM did not swing at that event (no change in risk).

We focus on events where \( S_t \) exceeds a minimum threshold
(e.g., \( S_t \ge S_{\min} \)) so that tiny, incidental tweaks are ignored.

---

## 3. Realized P&L per Unit of Risk

For each event \( t \) where the model swings:

- Define a realized or ground-truth **P&L per unit of risk** over the
  relevant horizon after the event:

\[
\Pi_t = \frac{\text{P\&L attributable to this position after event } t}
              {\text{risk units carried after the swing}}
\]

In practice, for eval purposes:

- \( \Pi_t \) can come from:
  - A simulated path with specified returns,
  - A labeled “good / bad / neutral” outcome mapped to numeric payoffs,
  - Historical data if you build a real backtest later.
- The key requirement is that, given the **thesis direction** (long or short),
  you can label whether the swing was a **winner** or a **loser**.

Classification:

- **Winning swing**: the swing increased exposure in a direction that generated
  positive P&L per risk unit (or reduced exposure ahead of negative P&L).
- **Losing swing**: the swing increased exposure into negative P&L per risk
  unit (or cut exposure ahead of positive P&L).

Formally:

- Winner set \( W = \{ t : S_t \ge S_{\min}, \Pi_t \text{ aligns with the thesis} \} \)
- Loser set  \( L = \{ t : S_t \ge S_{\min}, \Pi_t \text{ goes against the thesis} \} \)

---

## 4. Conviction Slugging Metric

Define:

- Average P&L per risk on **winning swings**:

\[
\overline{\Pi}_{W} =
\frac{1}{|W|} \sum_{t \in W} \Pi_t
\]

- Average absolute P&L per risk on **losing swings**:

\[
\overline{|\Pi|}_{L} =
\frac{1}{|L|} \sum_{t \in L} |\Pi_t|
\]

Then the **Conviction Slugging Score** is:

\[
\text{ConvictionSlugging} =
\frac{\overline{\Pi}_{W}}
     {\overline{|\Pi|}_{L}}
\]

Interpretation:

- > 1.0 : winners, on average, pay more per unit of risk than losers cost.  
- ~1.0 : symmetric payoff power; not great, not terrible.  
- < 1.0 : bad slugging; losers hurt more than winners help.

This mirrors the portfolio-level notion: payoff power per unit of risk when
the PM actually swings.

---

## 5. Conviction Slugging with Swing Size

We can also weight swings by **swing size** to reflect that:

- A big, well-timed swing should count more than a tiny add/trim.
- A big, wrong swing should hurt more.

Define **swing-weighted P&L per risk**:

\[
\Pi_t^{(w)} = S_t \cdot \Pi_t
\]

Then:

\[
\overline{\Pi}^{(w)}_{W} =
\frac{1}{\sum_{t \in W} S_t} \sum_{t \in W} S_t \cdot \Pi_t
\]

\[
\overline{|\Pi|}^{(w)}_{L} =
\frac{1}{\sum_{t \in L} S_t} \sum_{t \in L} S_t \cdot |\Pi_t|
\]

and the **Swing-Weighted Conviction Slugging** is:

\[
\text{ConvictionSlugging}^{(w)} =
\frac{\overline{\Pi}^{(w)}_{W}}
     {\overline{|\Pi|}^{(w)}_{L}}
\]

This variant emphasizes the quality of **large conviction moves**.

---

## 6. Practical Use in This Repo

In this repo, Conviction Slugging is intended as an **experimental metric**
to sit alongside:

- The discrete rubric (`earnings_research_thesis_and_risk_v1.md`),
- The continuous/dynamic scoring (`*_continuous.md`),
- The Bayesian framework (`*_bayesian.md`).

A typical usage pattern:

1. Define a scenario and event path.
2. Specify, for each event:
   - Ground-truth P&L outcome per risk unit for the thesis direction.
3. Have the model:
   - Propose an initial size in risk units,
   - Update size at each event (swing decisions).
4. Compute:
   - Which swings were winners vs losers,
   - Conviction Slugging and Swing-Weighted Conviction Slugging.

You can then compare models on:

- **Rubric scores** (reasoning, risk awareness, structure),
- **Bayesian conviction trajectories** (prior/posterior beliefs),
- **Conviction Slugging** (payoff power of their risk usage over the path).

The goal is to move beyond “did the model sound smart?” toward
“did the model **use risk intelligently** when it decided to swing?”
