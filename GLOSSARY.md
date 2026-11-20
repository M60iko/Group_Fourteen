# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| `Umsatz` (turnover) | Turnover of one product group on one day; the forecast target | Currency not stated in the source | Used as a stand-in for the baking quantity: the data has no unit counts. Turnover is what was sold, not what customers wanted (sold-out days hide demand). |
| `Warengruppe` (product group) | Product group code | 1 bread, 2 rolls, 3 croissants, 4 confectionery, 5 cakes, 6 seasonal bread | Group 6 only from late October to early January; group 4 has no rows on 53 days. |
| `Datum` (date) | Calendar date of the sales day | `YYYY-MM-DD` | Only days with sales have rows; 38 days have no sales at all. |
| Moment of prediction | When the forecast for tomorrow is made | Closing time of the day before | Sales up to and including today are known. |
| Next-day forecast | Forecast of tomorrow's turnover per product group, made at closing time | – | The main use case of the project. |
| Kaggle variant | Forecast of 01.08.2018 – 31.07.2019 for the course competition | – | No sales are known in that year, so recent sales cannot be features. Evaluated separately. |
| HICP | Harmonised Index of Consumer Prices (Eurostat), Germany | Index, 2015 = 100 | `hicp_all_items` = all items, `hicp_bread_cereals` = bread and cereals. Monthly; published after the month ends. |
| Inflation rate | Change of the HICP compared with the same month one year earlier | % | `inflation_all_items_pct`, `inflation_bread_cereals_pct`; starts in 01/2013. Not the same as the bakery's own price changes. |
| MAPE | Mean absolute percentage error: average of abs(actual − forecast) / actual | % | Course metric. Large for small values, e.g. seasonal bread. |
| MAE | Mean absolute error: average of abs(actual − forecast) | Turnover | The error in the unit of turnover; shows how big the error is in money terms. |
| Daily total | Sum of the turnover of all product groups on one day | Turnover | Evaluated with MAPE and MAE next to the per-group values. |
| Training / validation / test | Time-based split of the data | 01.07.2013 – 31.07.2017 / 01.08.2017 – 31.07.2018 / Kaggle file | Never split randomly. |
| Baseline (same weekday last week) | Forecast = turnover of the same product group seven days earlier | – | Stands for current practice; every model must beat it. |
