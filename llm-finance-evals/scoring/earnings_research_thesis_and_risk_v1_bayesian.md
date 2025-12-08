# Bayesian Scoring Framework: Earnings Research Thesis and Risk (v1)

This document defines an **explicit Bayesian framing** for evaluating model
outputs on the `earnings_research_thesis_and_risk_v1` task.

It does **not** replace the discrete or continuous rubrics. Instead, it
adds a third, more formal layer that:

- Treats conviction as a **probabilistic belief** that the thesis is
  economically “right” (not just well-written).
- Uses **Bayesian updates** to revise that belief as new information
  (events) arrives.
- Maps posterior beliefs into **position size in risk units**.

The goal is conceptual clarity: to show how discrete scores and conviction
updates can be embedded in an explicit prior/posterior framework.

---

## 1. State Variables

We introduce a small set of latent variables that represent beliefs about
the idea and its implementation:

- \( \theta_t \in [0, 1] \) – probability that the **thesis is economically right**
  at iteration \( t \). (“If I could replay the future many times, in what
  fraction of worlds is this thesis broadly correct?”)

- \( \psi_t \in [0, 1] \) – probability that the **sizing and risk usage are
  appropriate** at iteration \( t \). (“Given the thesis, how often does this
  sizing / risk budget lead to acceptable risk-adjusted outcomes?”)

- \( R_t \ge 0 \) – **risk units allocated** to the position at iteration \( t \)
  (e.g., from 0 to a maximum risk budget for this idea).

At any iteration \( t \), the system state is:

\[
S_t = (\theta_t, \psi_t, R_t)
\]

The Bayesian framework defines:

1. A **prior** over \( (\theta_0, \psi_0) \),
2. A set of **event types** with likelihoods conditional on \( \theta, \psi \),
3. An update rule (Bayes’ theorem) that produces **posterior** beliefs
   after each event.

---

## 2. Prior Specification

For simplicity, we assume independent Beta priors for thesis correctness
and sizing appropriateness:

- \( \theta_0 \sim \text{Beta}(a_\theta, b_\theta) \)
- \( \psi_0 \sim \text{Beta}(a_\psi, b_\psi) \)

Interpretation:

- \( a_\theta \) – prior “pseudo-successes” (cases where similar theses worked).
- \( b_\theta \) – prior “pseudo-failures” (cases where similar theses failed).

Example defaults (illustrative):

- \( a_\theta = 2, b_\theta = 2 \) → prior mean \( E[\theta_0] = 0.5 \)
  (agnostic but with some structure).
- \( a_\psi = 2, b_\psi = 3 \) → prior mean \( E[\psi_0] = 0.4 \)
  (assume sizing is often too aggressive or poorly aligned ex-ante).

Model outputs at iteration 0 (initial thesis) can be used to **inform these
priors** by mapping discrete/continuous rubric scores into pseudo-counts,
but the default version can simply start from fixed priors as above.

---

## 3. Event Types and Signals

We define events as **information shocks** that arrive along the event path
(e.g., for this eval: earnings, guidance, management commentary, modest
price reactions, risk reports).

Each event \( E_t \) is categorized as:

- **Supportive** of the thesis and/or sizing (e.g., results broadly in line
  with the base case or better, with no new risk flags).
- **Neutral / ambiguous** relative to the thesis.
- **Adverse** (e.g., evidence that weakens key drivers, raises risk, or shows
  sizing is misaligned vs realized volatility/drawdown).

For the Bayesian model, we treat each event as a **Bernoulli-style signal**
for \( \theta \) and \( \psi \):

- For thesis correctness \( \theta \):
  - supportive event → “success” signal,
  - adverse event    → “failure” signal,
  - neutral          → very small or no update.

- For sizing appropriateness \( \psi \):
  - supportive event (e.g., realized risk within budget, drawdowns consistent
    with plan) → “success”,
  - adverse event (e.g., outsized drawdown relative to risk budget,
    unanticipated factor exposure) → “failure”.

This is intentionally coarse but easy to extend.

---

## 4. Likelihood Model and Beta–Bernoulli Updates

Assume that, conditional on \( \theta \), each thesis-related event is drawn
from a Bernoulli process where a “success” is more likely if the thesis is
correct.

Similarly, conditional on \( \psi \), each sizing-related event is drawn from
a Bernoulli process where a “success” is more likely if sizing is appropriate.

Instead of specifying detailed likelihood functions, we use standard
**Beta–Bernoulli conjugacy**:

- For thesis correctness:

  - Prior: \( \theta_t \sim \text{Beta}(a_{\theta,t}, b_{\theta,t}) \)
  - After a supportive event (success):  
    \( a_{\theta,t+1} = a_{\theta,t} + 1 \), \( b_{\theta,t+1} = b_{\theta,t} \)
  - After an adverse event (failure):  
    \( a_{\theta,t+1} = a_{\theta,t} \), \( b_{\theta,t+1} = b_{\theta,t} + 1 \)
  - After a neutral event: optional small fractional update or no change.

- For sizing appropriateness (same pattern):

  - Prior: \( \psi_t \sim \text{Beta}(a_{\psi,t}, b_{\psi,t}) \)
  - Supportive event (risk behavior consistent with plan):  
    \( a_{\psi,t+1} = a_{\psi,t} + 1 \)
  - Adverse event (risk behavior worse than plan):  
    \( b_{\psi,t+1} = b_{\psi,t} + 1 \)
  - Neutral event: optional small/no update.

Posterior means after each event:

\[
E[\theta_{t+1}] = \frac{a_{\theta,t+1}}{a_{\theta,t+1} + b_{\theta,t+1}}
\]

\[
E[\psi_{t+1}] = \frac{a_{\psi,t+1}}{a_{\psi,t+1} + b_{\psi,t+1}}
\]

These posterior means are the **Bayesian conviction levels** for thesis and
sizing at iteration \( t+1 \).

---

## 5. Mapping Events from the Eval into Bayesian Updates

Within `earnings_research_thesis_and_risk_v1`, we can map specific event
types to thesis and sizing signals:

Examples for **thesis correctness (\( \theta \))**:

- Earnings broadly in line with thesis assumptions, guidance reiterated:  
  → supportive thesis event (success).
- Data showing slowed growth, shrinking TAM, or new competitive pressure,
  vs thesis assumptions:  
  → adverse thesis event (failure).
- Mixed signals or small deviations:  
  → neutral or very mild update.

Examples for **sizing / risk usage (\( \psi \))**:

- Realized volatility and drawdown in line with risk budget, factor and
  idiosyncratic contributions near expectations:  
  → supportive sizing event (success).
- Drawdown materially larger than expected for allocated risk units, or
  unexpected factor bets dominating P&L:  
  → adverse sizing event (failure).
- Small overshoots/undershoots vs budget:  
  → neutral / mild update.

The evaluator (or a scoring script) can encode these mappings as rules or
heuristics; the Bayesian layer provides the structure for updating beliefs.

---

## 6. Posterior to Risk Units: Sizing Rule

We now connect posterior beliefs to **risk allocation**.

Let:

- \( B_{\text{max}} \) – maximum risk units allowed for this idea (e.g., 5 units).
- \( \theta_t^\* = E[\theta_t] \) – posterior mean for thesis correctness.
- \( \psi_t^\* = E[\psi_t] \) – posterior mean for sizing appropriateness.

A simple sizing rule:

1. Define a combined conviction measure, for example:
   \[
   C_t = \theta_t^\* \times \psi_t^\*
   \]
   or a weighted average:
   \[
   C_t = w_\theta \, \theta_t^\* + w_\psi \, \psi_t^\*, \quad w_\theta + w_\psi = 1
   \]

2. Map conviction to risk units:
   \[
   R_t = B_{\text{max}} \times C_t
   \]

3. Optionally impose bands or thresholds, e.g.:
   - If \( C_t < 0.3 \) → position should be very small or zero.
   - If \( 0.3 \le C_t < 0.6 \) → small to medium risk allocation.
   - If \( C_t \ge 0.6 \) → allow up to full risk budget (subject to
     portfolio-level constraints).

This creates a **direct linkage**:

- Strong thesis + good sizing track record (high posteriors) → more risk units.
- Weak thesis or poor sizing track record → fewer risk units, even if one
  of the two looks good.

---

## 7. Integration with Discrete and Continuous Rubrics

The Bayesian layer is meant to **sit on top of**, or alongside, the existing
rubrics:

- **Discrete rubric (`*_v1.md`)**  
  - Used for initial evaluation of a single answer at iteration 0.
  - Can be mapped to initial Beta parameters:
    - Higher discrete scores on thesis-related dimensions could increase
      \( a_\theta \) relative to \( b_\theta \),
    - Higher scores on sizing-related dimensions could increase \( a_\psi \)
      relative to \( b_\psi \).

- **Continuous / dynamic rubric (`*_continuous.md`)**  
  - Provides smooth score updates per iteration.
  - Its continuous scores and conviction trajectories can be treated as
    **derived observables** or as an intermediate layer that informs how we
    categorize events (supportive/neutral/adverse) for the Bayesian updates.

- **Bayesian rubric (this file)**  
  - Explicitly formalizes prior/posterior belief about thesis correctness
    and sizing quality.
  - Gives a clear, interpretable rule for how much risk the PM “should”
    allocate given current beliefs.

You can implement any subset of these layers; the bayesian file is designed
to be compatible with both.

---

## 8. Simple Illustrative Example

Very simplified schematic:

- Start with priors:
  - \( \theta_0 \sim \text{Beta}(2, 2) \Rightarrow E[\theta_0] = 0.5 \)
  - \( \psi_0 \sim \text{Beta}(2, 3) \Rightarrow E[\psi_0] = 0.4 \)
  - \( B_{\text{max}} = 5 \) risk units

- Event 1 (earnings) – broadly supportive of thesis, risk behavior in line
  with plan:
  - Thesis: success → \( a_{\theta,1} = 3, b_{\theta,1} = 2 \Rightarrow E[\theta_1] = 0.6 \)
  - Sizing: success → \( a_{\psi,1} = 3, b_{\psi,1} = 3 \Rightarrow E[\psi_1] = 0.5 \)

- Combined conviction:
  - \( C_1 = \theta_1^\* \times \psi_1^\* = 0.6 \times 0.5 = 0.30 \)
  - Implied risk units \( R_1 = 5 \times 0.30 = 1.5 \) units

- Event 2 (guidance + flows) – mixed fundamentals but increasing crowding
  and some risk-budget stress:
  - Thesis: ambiguous (no update) → \( E[\theta_2] \approx 0.6 \)
  - Sizing: adverse (failure) → \( a_{\psi,2} = 3, b_{\psi,2} = 4 \Rightarrow E[\psi_2] \approx 0.43 \)
  - \( C_2 \approx 0.6 \times 0.43 \approx 0.258 \)
  - \( R_2 \approx 5 \times 0.258 \approx 1.29 \) risk units → suggests a **trim**, even with thesis unchanged.

This illustrates key points:

- The thesis can remain broadly intact,
- But posterior beliefs about **sizing appropriateness** can deteriorate,
- Leading to a lower **risk allocation** = what a PM could/should
  do in the face of worsening realized risk behavior or crowding—even if
  they still like the idea.

---

This Bayesian rubric is intentionally self-contained and conceptual. It
shows how the evaluation framework can be extended from **discrete scores**
→ **continuous conviction trajectories** → **explicit Bayesian priors and
posteriors** that directly govern risk allocation in a long/short book.
