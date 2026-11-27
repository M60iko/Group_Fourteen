# Bakery data fact sheet

This summary combines the two November 2026 data profiles. The [data profile notebook](../1_DatasetCharacteristics/data_profile.ipynb) records the input fingerprints and detailed counts.

## Sources and joins

| Source | Rows | Coverage | Key |
|---|---:|---|---|
| Sales (`umsatzdaten_gekuerzt.csv`) | 9,334 | 2013-07-01 to 2018-07-31 | `Datum` + `Warengruppe` and `id` are both unique. Each ID matches `YYMMDD` + group. |
| Weather (`wetter.csv`) | 2,601 | 2012-01-01 to 2019-08-01, with 169 dates missing | One row per `Datum` |
| Kiel Week (`kiwo.csv`) | 72 | Nine event dates per year from 2012 through 2019 | One row per event `Datum` |
| German inflation (`inflation_germany_monthly.csv`) | 91 | Every month from 2012-01 through 2019-07 | One row per `month` |

The course attributes the bakery files to meteolytix GmbH and lists no dataset-specific license. The inflation file contains Eurostat HICP indices for all items and bread and cereals (2015 = 100), plus year-on-year rates. The first 12 months lack prior-year values for calculating those rates. [Course dataset documentation](https://github.com/opencampus-sh/intro-to-data-science-and-ml/blob/main/data/bakery/README.md) · [Inflation download notebook](../0_DataPreparation/inflation_germany.ipynb)

Left joins retain all 9,334 sales rows. Weather matches 1,816 sales dates and 9,318 rows. Kiel Week matches 45 dates across five editions and 223 rows. The course uses 0 for dates outside the listed events within the covered years. Both tested HICP joins (sales month minus one and minus two) match all sales rows. Holiday sources and Kaggle test keys still need verification.

## Sales and weather gaps

Sales fields have no blanks. Recorded turnover ranges from 7.05 to 1,879.46, with a median of 161.9. There are sales on 1,819 of 1,857 calendar dates. The 38 dates with no rows include recurring holidays, but the records alone cannot establish why sales are absent.

| Product group | Recorded days | Absent days with other sales | Median turnover |
|---|---:|---:|---:|
| Bread | 1,819 | 0 | 120.05 |
| Rolls | 1,819 | 0 | 370.83 |
| Croissants | 1,819 | 0 | 142.81 |
| Confectionery | 1,766 | 53 | 79.99 |
| Cakes | 1,819 | 0 | 265.96 |
| Seasonal bread | 292 | 1,527 | 62.91 |

Confectionery gaps occur in 2013 (16), 2014 (23), 2015 (10) and 2016 (4). Seasonal bread sales appear in October (13 days), November (140), December (133) and January (6). The sales records establish when it sold. Historical offer dates still need confirmation. The maximum cake turnover of 1,879.46 warrants review before any outlier treatment.

Three sales dates have no weather row (2016-12-11, 2017-10-04 and 2017-10-05), affecting 16 sales rows. Across the full weather file, cloud cover is blank on 10 dates (54 matching sales rows) and weather code on 669 dates (2,309 matching sales rows). Blank codes occur more often in warmer, less cloudy conditions during the sales period. The course suggests they may signify no notable weather. Code 0 also occurs explicitly, so the meaning of blanks needs confirmation. Recorded wind values range from 3 to 35, and the documented m/s unit needs confirmation.

## Forecast evaluation

The agreed training period (2013-07-01 through 2017-07-31) has 7,493 rows. Validation (2017-08-01 through 2018-07-31) has 1,841. The same-product-group, same-weekday baseline is missing an exact seven-day match for 248 training rows and 42 validation rows.

The operations manager forecasts at the prior day's closing time and includes seasonal bread only on offer days. Observed weather is the agreed stand-in for tomorrow's forecast in historical evaluation and may make results optimistic. HICP coverage in the file does not establish availability at closing time. A one-month lag can use figures before publication, especially early in the month. A two-month lag from prediction time is a conservative option pending approval. [Canvas](../CANVAS.md) · [Decision log](../DECISIONS.md) · [Eurostat release information](https://ec.europa.eu/eurostat/web/hicp/information-data)

The separate Kaggle variant covers August 2018 through July 2019 and uses sales only through July 2018. The team still needs the test file and an external-data cutoff. The historical data supports turnover forecasts and comparisons across calendar and weather conditions. Inflation associations cannot establish a causal effect, and the data lacks unit sales, unmet demand, branch prices and promotions.

## Open decisions and proposed checks

- Confirm how to handle absent sales, identify days eligible for daily-total scoring and obtain an independent offer calendar or approve a rule for seasonal bread. If verified gaps are filled with zero, agree how MAPE handles zero actuals.
- Agree on weather gap handling and code encoding, verify the wind unit and decide how to handle unusually high turnover. Confirm historical Schleswig-Holstein public and school holiday sources and scope.
- Confirm how to use inflation and which publication cutoff applies. Agree on baseline fallback or shared scoring coverage, and verify Kaggle keys when the test file is available.
- Proposed checks cover unique keys and valid group codes, positive observed turnover, left-join row counts and gap flags, binary Kiel Week flags, fixed date splits, comparable baseline and model coverage, and feature availability at the prediction cutoff. Fit any preprocessing on training data only.
