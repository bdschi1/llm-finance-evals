# Example Input: ML Pipeline and Backtest Sanity Check (v1)

This document describes a **toy long–short equity factor strategy** and its
data / ML / backtest pipeline. It intentionally contains several common
pitfalls for the model to detect and fix.

---

## 1. Strategy Overview

- Universe: current members of the S&P 500 index.
- Horizon: 1-day holding period, rebalanced **daily**.
- Objective: maximize Sharpe ratio of a dollar-neutral long–short portfolio.

The strategy predicts each stock’s **next-day return** using a set of
cross-sectional signals, then goes long the top decile and short the bottom
decile each day, equally weighted within each side.

---

## 2. Data Pipeline

- Data vendor: commercial price and fundamental database.
- Universe: **constituents of the S&P 500 as of 31 Dec 2024**.
- History: daily data from 2010-01-01 to 2024-12-31.
- Fields:
  - Daily open, high, low, close, volume.
  - Quarterly EPS, book value, and sales.
- All data pulled as a single panel and joined on `(ticker, date)`.

Pre-processing steps:

1. Drop any days where the close price is missing.
2. Forward-fill missing fundamentals until the next reported quarter.
3. Filter out stocks with price < $5.
4. Keep only stocks that appear in the 2024 S&P 500 universe file.

No explicit handling of:

- Delistings,
- Corporate actions (splits, dividends),
- Index membership over time.

---

## 3. Feature and Label Construction

For each stock *i* on each trading day *t*:

- **Features**

  - 12-month momentum:  
    `mom_12m = close(t) / close(t-252) - 1`
  - 1-month momentum:  
    `mom_1m = close(t) / close(t-21) - 1`
  - Earnings yield:  
    `ey = EPS_ttm(t) / close(t)`
  - Book-to-price:  
    `bp = book_value_mrq(t) / close(t)`
  - Size:  
    `size = log(market_cap(t))`

- **Label**

  - Next-day return:  
    `label = close(t+1) / close(t) - 1`

To simplify alignment, all features and labels are computed from the same
merged panel, using standard (non point-in-time) adjusted fields.

There is no explicit check that **only information available at time t** is
used when creating features or labels.

---

## 4. Model and Training Setup

- Model: gradient boosted trees (GBM).
- Training window: 2010-01-01 to 2020-12-31.
- Validation / test window: 2021-01-01 to 2024-12-31.

Training process:

1. Split the **training period** randomly into 5 folds (random shuffle of
   dates) and perform 5-fold cross-validation to tune tree depth,
   learning rate, and number of trees.
2. After hyperparameters are chosen, train a final GBM on the **full
   2010–2020 training period**.
3. Apply this model to 2021–2024 to generate predicted next-day returns.

The CV process treats all `(stock, date)` pairs as i.i.d. records and does
not enforce time ordering.

---

## 5. Backtest Design

Daily loop for 2021–2024:

1. For each date *t*, use the trained model to predict `label_hat(i, t)` for
   all stocks in the universe.
2. Rank stocks by predicted return.
3. Go **long** the top 10% and **short** the bottom 10%, with:
   - Equal weights within each side,
   - Gross exposure fixed at 200% (100% long, 100% short),
   - Net exposure ~0%.
4. Compute portfolio return for day *t+1* as the average realized return of
   longs minus shorts.

Assumptions:

- No transaction costs or slippage.
- All orders filled at the **next day close price**.
- No constraints on position size, turnover, or liquidity.
- No delays between signal computation and trade execution.

Performance reporting:

- Daily returns aggregated into:
  - Annualized return,
  - Annualized volatility,
  - Sharpe ratio,
  - Maximum drawdown.
- Only the 2021–2024 period is used to report performance.

---

## 6. Risk and Capacity

Risk analysis:

- Compute portfolio volatility and maximum drawdown over 2021–2024.
- No decomposition by sector, factor, or single-name contributions.
- No analysis by market regime (e.g., low vs high volatility periods).

Capacity considerations:

- Assume the strategy is scalable to at least USD 5 billion AUM because
  it trades “large, liquid S&P 500 names.”
- No explicit checks on:
  - Turnover,
  - Dollar volume traded,
  - Ownership limits or crowding.

---

## 7. Summary of Open Questions (Implicit)

The description above leaves several aspects unspecified or simplified,
including:

- How the S&P 500 universe is constructed through time.
- Whether the data fields are point-in-time and free of survivorship bias.
- Whether the feature/label construction uses only information available at
  decision time.
- Whether the random cross-validation scheme is appropriate for time series.
- How realistic the backtest is once transaction costs, trade delays,
  and constraints are considered.

The eval task is to **critically review this pipeline**, identify issues,
and propose concrete fixes and redesign steps.
