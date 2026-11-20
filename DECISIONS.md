# Decisions

Newest first. One entry per decision taken at a stop point.

## 2026-11-20: Inflation is added as a data source
**Canvas block:** 2, 5, 6
**Decision:** Monthly inflation for Germany (Eurostat HICP, all items and bread and cereals) is added as an additional data source.
**Reason:** Team request; turnover is measured in money, so price changes may shift it.
**Alternatives considered:** National CPI of Destatis (VPI), not used because the Eurostat series is openly downloadable without a login; both measure German consumer prices. The period was extended from 2013 – 2018 to 01/2012 – 07/2019 for the year-on-year rate, the one-month delay and the Kaggle test year.
**Decided by:** Marco, Aia, Maria, Rebecca (delay and use still open, see canvas)

## 2026-11-20: What is known in advance
**Canvas block:** 6
**Decision:** Features may use sales up to and including today, tomorrow's calendar, whether seasonal bread is on offer, and the weather forecast (observed weather as a stand-in). Tomorrow's sales and anything computed from them are excluded. In the Kaggle variant no sales after 31.07.2018 are used.
**Reason:** The forecast is made at closing time of the day before; everything else would be leakage.
**Alternatives considered:** Leaving weather out because only observed weather exists, rejected; it is kept and named as a slightly optimistic stand-in.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Time-based data split
**Canvas block:** 4, 6
**Decision:** Training 01.07.2013 – 31.07.2017, validation 01.08.2017 – 31.07.2018, test = Kaggle file.
**Reason:** A time series must be split by date so that the model never learns from the future.
**Alternatives considered:** Random split, rejected because it leaks future information.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Success criterion
**Canvas block:** 4
**Decision:** A model must beat the baseline (same weekday last week) at least on the daily total of all groups; the goal is to beat it in every group.
**Reason:** The total matters most for the daily plan; groups where the model is worse are reported openly.
**Alternatives considered:** Requiring a win in every group (agent's recommendation), relaxed to the total as the minimum.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Over- and under-baking weighed equally for now
**Canvas block:** 4
**Decision:** Both kinds of error count the same until the client says otherwise.
**Reason:** There is no cost data; MAPE and MAE are symmetric.
**Alternatives considered:** An asymmetric metric, postponed until costs are known.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Metrics
**Canvas block:** 4
**Decision:** MAPE and MAE (error in turnover), each per product group and for the daily total of all groups, on validation data next to the training score.
**Reason:** MAPE is the course metric; MAE shows the size of the error in turnover; the total shows the quality of the whole daily plan.
**Alternatives considered:** MAPE per group only (agent's recommendation), extended by the team.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Seasonal bread is included
**Canvas block:** 1
**Decision:** All six product groups are forecast. Seasonal bread is forecast only on days when it is on offer.
**Reason:** The operations manager knows in advance whether it is on offer, and the course asks for the MAPE of all six groups.
**Alternatives considered:** Leaving seasonal bread out (only about 1% of turnover), rejected because it is part of the decision and the evaluation.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: The canvas covers the next-day decision; Kaggle is a separate variant
**Canvas block:** 1, 4
**Decision:** The canvas describes the real forecast for tomorrow. The Kaggle forecast (08/2018 – 07/2019) is evaluated as a separate variant.
**Reason:** In the Kaggle year no sales are known, so the two variants have different rules for what is known in advance. Keeping them apart avoids leakage.
**Alternatives considered:** One canvas for the Kaggle task only, rejected because it does not match the client's daily decision.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Baseline is the same weekday of the previous week
**Canvas block:** 1, 4
**Decision:** Current practice is taken to be "the same as on the same weekday of the previous week", and this rule is the baseline every model must beat.
**Reason:** It describes how the operations manager decides today.
**Alternatives considered:** Yesterday's turnover as baseline, not chosen because it ignores the weekly pattern.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Decision is made at closing time
**Canvas block:** 1, 6
**Decision:** The amounts for tomorrow are set once a day at closing time.
**Reason:** Team decision. As a consequence, today's sales are complete and may be used for the forecast.
**Alternatives considered:** Around 2 pm (agent's recommendation), when today's sales would still be incomplete.
**Decided by:** Marco, Aia, Maria, Rebecca

## 2026-11-20: Turnover is the stand-in for the baking quantity
**Canvas block:** 1
**Decision:** The analysis forecasts turnover per product group; the operations manager converts it into baking quantities.
**Reason:** The data has no unit counts, costs or unsold goods.
**Alternatives considered:** Forecasting quantities directly, not possible with this data.
**Decided by:** Marco, Aia, Maria, Rebecca

<!--
## YYYY-MM-DD: <short title>
**Canvas block:** <number>
**Decision:** <what was decided>
**Reason:** <why>
**Alternatives considered:** <what else, and why not>
**Decided by:** <names>
-->
