"""
Code stub corresponding to the ML pipeline described in
ml_pipeline_and_backtest_sanity_check_v1_example.md.

This is intentionally simplified and mirrors the same design choices,
including some that are problematic. It is not meant to be run as-is;
it is provided so an evaluator can see the rough structure.
"""

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import GradientBoostingRegressor

# Load pre-merged panel (current S&P 500 universe, 2010-2024)
panel = pd.read_parquet("sp500_panel_2010_2024.parquet")

# Basic cleaning
panel = panel[panel["close"].notna()]
panel = panel[panel["close"] >= 5.0]

# Forward-fill fundamentals
fund_cols = ["eps_ttm", "book_value_mrq", "sales_ttm"]
panel[fund_cols] = panel.groupby("ticker")[fund_cols].ffill()

# Feature construction
panel["mom_12m"] = panel.groupby("ticker")["close"].pct_change(252)
panel["mom_1m"] = panel.groupby("ticker")["close"].pct_change(21)
panel["ey"] = panel["eps_ttm"] / panel["close"]
panel["bp"] = panel["book_value_mrq"] / panel["close"]
panel["size"] = (panel["shares_out"] * panel["close"]).pipe(lambda mkt_cap: mkt_cap.clip(lower=1)).apply(lambda x: np.log(x))

# Label: next-day return
panel["label"] = panel.groupby("ticker")["close"].pct_change(-1)

# Drop rows with missing features/label
features = ["mom_12m", "mom_1m", "ey", "bp", "size"]
panel = panel.dropna(subset=features + ["label"])

# Train/validation split by date (but CV is random)
train_mask = panel["date"] < "2021-01-01"
train = panel[train_mask]
test = panel[~train_mask]

X_train = train[features].values
y_train = train["label"].values
X_test = test[features].values
y_test = test["label"].values

# Random 5-fold CV on all (ticker, date) rows
kf = KFold(n_splits=5, shuffle=True, random_state=42)

best_params = None
best_score = -1e9

for max_depth in [3, 5]:
    for learning_rate in [0.05, 0.1]:
        fold_scores = []
        for train_idx, val_idx in kf.split(X_train):
            model = GradientBoostingRegressor(
                max_depth=max_depth,
                learning_rate=learning_rate,
                n_estimators=200,
            )
            model.fit(X_train[train_idx], y_train[train_idx])
            preds = model.predict(X_train[val_idx])
            fold_scores.append(preds.mean())  # placeholder "score"
        avg_score = sum(fold_scores) / len(fold_scores)
        if avg_score > best_score:
            best_score = avg_score
            best_params = (max_depth, learning_rate)

# Final model on full training set with best params
final_model = GradientBoostingRegressor(
    max_depth=best_params[0],
    learning_rate=best_params[1],
    n_estimators=200,
)
final_model.fit(X_train, y_train)

# Predict next-day return for 2021-2024
test["pred"] = final_model.predict(X_test)

# Backtest: each day, long top 10% and short bottom 10%, equal-weight, no costs
def daily_portfolio_return(df_day):
    df_day = df_day.sort_values("pred")
    n = len(df_day)
    k = max(1, n // 10)
    shorts = df_day.head(k)
    longs = df_day.tail(k)
    long_ret = longs["label"].mean()
    short_ret = shorts["label"].mean()
    return long_ret - short_ret

daily_returns = test.groupby("date").apply(daily_portfolio_return)

# Compute summary stats (ignoring costs, delays, constraints)
ann_ret = daily_returns.mean() * 252
ann_vol = daily_returns.std() * (252 ** 0.5)
sharpe = ann_ret / ann_vol if ann_vol > 0 else 0.0

print("Annualized return:", ann_ret)
print("Annualized vol:", ann_vol)
print("Sharpe:", sharpe)
