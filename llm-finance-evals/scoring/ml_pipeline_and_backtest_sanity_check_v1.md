# Scoring Rubric: ML Pipeline and Backtest Sanity Check (v1)

This rubric scores model outputs for the `ml_pipeline_and_backtest_sanity_check_v1`
eval. Scores are on a **1–5** scale for each dimension, where:

- **1 – Poor**: misses key issues, reasoning is shallow or wrong.
- **2 – Weak**: catches one or two issues but misses most of what matters.
- **3 – Adequate**: identifies the main issues with limited depth or incomplete fixes.
- **4 – Strong**: catches most important issues with good explanations and fixes.
- **5 – Expert**: comprehensive, precise, and clearly written; looks like a seasoned
  quant/PM reviewing the pipeline.

You may also translate these to continuous scores if you are using the continuous or
Bayesian scoring overlays.

---

## 1. Data Engineering Awareness

**What to look for**

- Mentions of:
  - Correct use of **adjusted prices** for splits/dividends.
  - **Survivorship bias** risk (e.g., using a current universe in historical backtests).
  - **Look-ahead bias** in labels, features, or data filters.
  - Proper handling of **identifiers** and mapping across sources.
  - Calendar alignment and handling of missing data.

**Scoring**

- **1** – Ignores all major data issues; accepts raw inputs at face value.
- **2** – Vague “data quality” comments with no concrete mention of survivorship,
  look-ahead, or corporate actions.
- **3** – Flags at least one major issue (e.g., survivorship or look-ahead) but misses
  others or offers limited remedies.
- **4** – Systematically checks the main data traps and proposes sensible fixes
  (e.g., point-in-time universe, adjusted prices, robust joins).
- **5** – Reads like a careful quant: clearly explains each risk, how it would bias P&L,
  and how to repair the pipeline step by step.

---

## 2. Feature & Label Reasoning

**What to look for**

- Alignment between:
  - Prediction **horizon** and label definition.
  - Feature construction and data frequency.
  - Cross-sectional vs time-series features.
- Awareness of:
  - Using only information available at decision time.
  - Avoiding engineered labels that leak future information.

**Scoring**

- **1** – No real critique of features or labels.
- **2** – Comments are generic (“maybe add more factors”) without time/horizon logic.
- **3** – Spots at least one horizon or leakage issue but does not fully clean it up.
- **4** – Explains how to redesign features/labels to respect timing and data frequency.
- **5** – Provides a clear, coherent redesign of the feature/label set that would make
  the strategy empirically testable and realistic.

---

## 3. Validation & Overfitting Control

**What to look for**

- Understanding of:
  - Train/validation/test splits or walk-forward schemes.
  - Cross-validation appropriate for time series.
  - Regularization and hyperparameter tuning.
  - Performance metrics suited to the objective (e.g., return, Sharpe, drawdown).

**Scoring**

- **1** – Accepts the existing validation as-is, or clearly wrong suggestions
  (e.g., random CV on time series with leakage).
- **2** – Vague mention of “use cross-validation” without time ordering or leakage
  considerations.
- **3** – Identifies some risk of overfitting but only partially addresses it.
- **4** – Recommends a reasonable validation / walk-forward process and regularization
  approach, with clear reasoning.
- **5** – Lays out a disciplined validation plan that a professional quant team could
  implement, including rationale for metrics and monitoring.

---

## 4. Backtest Realism

**What to look for**

- Treatment of:
  - Rebalancing frequency and order of operations.
  - Transaction costs and slippage.
  - Liquidity and capacity constraints.
  - Shorting constraints, leverage, and margin.
  - Delay between signal computation and execution.

**Scoring**

- **1** – Treats backtest results as if they were real P&L; no mention of costs or
  constraints.
- **2** – Mentions “add costs” without specifying how or where they matter.
- **3** – Identifies at least one major bias (e.g., ignoring costs or trade delay) but
  leaves gaps.
- **4** – Describes a more realistic backtest configuration and how it will change
  expectations (e.g., lower Sharpe, slower turnover).
- **5** – Demonstrates a deep understanding of how implementation details distort P&L,
  and proposes a clean redesign that would stand up in an investment committee.

---

## 5. Risk & Capacity Thinking

**What to look for**

- Discussion of:
  - Volatility and drawdown.
  - Tail behavior and regime sensitivity (e.g., different performance in high/low vol).
  - Strategy **capacity** and turnover: where it likely saturates.
  - How the strategy would coexist in a larger long/short book or multi-strategy
    portfolio.

**Scoring**

- **1** – No mention of risk or capacity beyond “risk-adjusted return.”
- **2** – Mentions volatility or drawdown but in a superficial way.
- **3** – Recognizes at least one structural risk or capacity limit.
- **4** – Articulates how risk and capacity should be measured and monitored for this
  specific strategy.
- **5** – Integrates risk and capacity thinking into the critique so that the final
  recommendations are clearly portfolio-aware, not just backtest-aware.

---

## 6. Actionability of Recommendations

**What to look for**

- Concrete steps, phrased so an engineer or quant can act:
  - “Use point-in-time constituents from [source], not today’s index members.”
  - “Shift labels to t+1 daily returns and re-lag features to avoid leakage.”
  - “Implement a rolling walk-forward window with X months training, Y months test.”

**Scoring**

- **1** – Mostly vague platitudes (“improve data quality”, “use better model”).
- **2** – One or two concrete suggestions; rest is generic.
- **3** – Several concrete suggestions but missing prioritization or clarity.
- **4** – Clear, prioritized checklist of fixes with enough detail to implement.
- **5** – Reads like a focused review memo from a senior quant / PM to the research
  team, with a realistic implementation roadmap.

---

## Overall Score

You can combine the dimensions into an overall 1–5 score by weighted average.
Suggested weights (summing to 1.0):

- Data Engineering Awareness: 0.20  
- Feature & Label Reasoning: 0.20  
- Validation & Overfitting Control: 0.20  
- Backtest Realism: 0.20  
- Risk & Capacity Thinking: 0.10  
- Actionability of Recommendations: 0.10  

Document the overall score along with 2–3 key failure modes and 2–3 key strengths.
These qualitative notes are often more useful to model developers than the numeric
score itself.
