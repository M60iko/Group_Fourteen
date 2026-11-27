# Bakery data fact sheet

Profiled on 24 November 2026 by running all code cells of the [data profile notebook](../1_DatasetCharacteristics/data_profile.ipynb) in order. The notebook reads directly from GitHub and the local inflation CSV. It prints a SHA-256 fingerprint for each input.

## Sources and keys

| Source | Rows × columns | What one row represents | Candidate key and duplicates | Coverage |
|---|---:|---|---|---|
| `umsatzdaten_gekuerzt.csv` | 9,334 × 4 | Recorded daily turnover for one product group at a Kiel branch | `id` and `Datum` + `Warengruppe` are each unique. All IDs agree with the date and group. Date alone repeats. | 2013-07-01 to 2018-07-31. There are 1,819 of 1,857 calendar days. Calendar year 2013 starts in July and 2018 ends in July. |
| `wetter.csv` | 2,601 × 5 | Daily weather observations in Kiel | `Datum` is unique. | 2012-01-01 to 2019-08-01. There are 169 gaps across 2,770 calendar days. The final year ends in August. |
| `kiwo.csv` | 72 × 2 | One Kiel Week event day | `Datum` is unique. | 2012-06-16 to 2019-06-30. Exactly nine event dates per year from 2012 to 2019. Other dates have no row by design. |
| `inflation_germany_monthly.csv` | 91 × 5 | One month of nationwide German price indices and derived inflation rates | `month` is unique. | 2012-01 through 2019-07, with every month present. The final year ends in July. |
| Kaggle test | Unverified | Expected date and product-group request | The course documents the ID format. Key coverage and uniqueness are unverified. | The course specifies 2018-08-01 to 2019-07-31. The file and competition link were unavailable in the repository. |
| Public and school holidays | Source pending | Expected Schleswig-Holstein calendar dates | Date after expanding ranges and resolving overlaps | The team needs to confirm sources and calendar scope. |

The course attributes the three bakery files to meteolytix GmbH. No dataset-specific license is stated in the course dataset documentation. Inflation comes from Eurostat HICP dataset `prc_hicp_midx`, series `CP00` and `CP0111`, via the [download notebook](../0_DataPreparation/inflation_germany.ipynb). [Course dataset documentation](https://github.com/opencampus-sh/intro-to-data-science-and-ml/blob/main/data/bakery/README.md) · [Eurostat HICP metadata](https://ec.europa.eu/eurostat/cache/metadata/en/prc_hicp_esms.htm)

## Columns and missing values

| Source | Column | Type and unit | Observed range or values | Blank cells |
|---|---|---|---|---:|
| Sales | `id` | Encoded identifier `YYMMDD` + group | 1307011–1807315 | 0 |
| Sales | `Datum` | ISO date | 2013-07-01–2018-07-31 | 0 |
| Sales | `Warengruppe` | Integer category | 1–6 | 0 |
| Sales | `Umsatz` | Decimal turnover, currency unspecified | 7.05–1,879.46 | 0 |
| Weather | `Datum` | ISO date | 2012-01-01–2019-08-01 | 0 |
| Weather | `Bewoelkung` | Integer octas of cloud cover | 0–8 | 10 |
| Weather | `Temperatur` | Decimal daily mean °C | −10.25–32.67 | 0 |
| Weather | `Windgeschwindigkeit` | Numeric daily mean wind speed, documented as m/s | 3–35 | 0 |
| Weather | `Wettercode` | Integer WMO present-weather category | 0–95, 41 distinct codes | 669 |
| Kiel Week | `Datum` | ISO event date | 2012-06-16–2019-06-30 | 0 |
| Kiel Week | `KielerWoche` | Integer event flag | 1 | 0 |
| Inflation | `month` | ISO month | 2012-01–2019-07 | 0 |
| Inflation | `hicp_all_items` | Decimal index, 2015 = 100 | 95.7–106.4 | 0 |
| Inflation | `hicp_bread_cereals` | Decimal index, 2015 = 100 | 93.2–105.3 | 0 |
| Inflation | `inflation_all_items_pct` | Decimal year-on-year % | −0.51–2.63 | 12 |
| Inflation | `inflation_bread_cereals_pct` | Decimal year-on-year % | 0.20–3.43 | 12 |

Both inflation rates are blank only in January–December 2012, when the file lacks the same month a year earlier. Observed turnover is positive in every row. The cloud and weather codes fall within their documented bounds. A daily mean wind speed of 35 m/s would be unusually high, so verify the reported unit and extremes with the source before converting values or excluding records.

### Absent sales rows

| Group | Recorded rows | Missing on days with other sales | Turnover min / median / max | Rows without a seven-day lag |
|---|---:|---:|---|---:|
| Bread | 1,819 | 0 | 23.11 / 120.05 / 416.79 | 40 |
| Rolls | 1,819 | 0 | 175.00 / 370.83 / 1,203.43 | 40 |
| Croissants | 1,819 | 0 | 37.74 / 142.81 / 565.94 | 40 |
| Confectionery | 1,766 | 53 | 27.43 / 79.99 / 430.50 | 87 |
| Cakes | 1,819 | 0 | 121.49 / 265.96 / 1,879.46 | 40 |
| Seasonal bread | 292 | 1,527 | 7.05 / 62.91 / 172.87 | 43 |

- **Whole days.** No sales rows appear on 38 dates, including recurring dates such as Christmas Day and New Year’s Day, plus dates such as 2016-07-07. The rows alone cannot establish whether the bakery closed or whether records were lost. The notebook prints the complete list.
- **Confectionery.** Its 53 absent dates with other sales occur in 2013 (16), 2014 (23), 2015 (10) and 2016 (4). The file contains no explanation for that concentration.
- **Seasonal bread.** Recorded months are October through January. A recorded sale establishes that the product sold on that date. A missing sale leaves historical availability uncertain. The operations manager can supply tomorrow’s offer status at closing time.
- **Evaluation coverage.** Training has 7,493 rows across 1,462 of 1,492 dates. Validation has 1,841 rows across 357 of 365 dates. The exact seven-day rule lacks an earlier row for 248 training rows and 42 validation rows, including where an earlier date falls before the file starts.

### Weather gaps and blank fields

- All weather fields are absent on 2016-12-11, 2017-10-04 and 2017-10-05. Those dates account for 16 sales rows.
- Cloud cover is blank on 10 weather dates, two in October and eight in November. Mean temperature is 9.48°C on those dates and 12.11°C on dates with a cloud value. Nine of the 10 dates match 54 sales rows.
- Weather code is blank on 669 weather dates. It is blank on 91 of 239 June dates and 22 of 200 December dates. Mean temperature is 15.44°C with a blank and 10.94°C when a code is present. The course suggests that blanks may indicate no notable weather. Code 0 appears as a recorded value, so equating it with a blank would need source confirmation. The blanks match 456 sales dates and 2,309 sales rows.

## Proposed joins measured against sales

Key shares use distinct dates or months. Sales-row counts include all recorded groups on matching dates.

| Right source and key | Matching left keys | Matching right keys | Sales rows with a match | Sales rows after left join |
|---|---:|---:|---:|---:|
| Weather on `Datum` | 1,816 / 1,819 (99.8%) | 1,816 / 2,601 (69.8%) | 9,318 | 9,334 |
| Kiel Week on `Datum` | 45 / 1,819 (2.5%) | 45 / 72 (62.5%) | 223 | 9,334 |
| HICP on sales month minus one | 61 / 61 (100%) | 61 / 91 (67.0%) | 9,334 | 9,334 |
| HICP on sales month minus two | 61 / 61 (100%) | 61 / 91 (67.0%) | 9,334 | 9,334 |

Weather joins by daily date. Kiel Week is a sparse event list, so the course specifies filling unmatched event flags with 0 within the documented years. HICP joins one monthly record to many sales rows. Both lag options have complete file coverage. File coverage alone cannot establish whether any particular value was published by prediction time. Holiday and Kaggle joins await source files.

## Questions the data can address

Q-a can be evaluated for recorded turnover on the historical validation period. Historical offer status, openings and completeness of daily totals require confirmation where rows are absent. Q-b can examine associations with calendar, weather and prices, with five Kiel Week editions represented in sales. Price indices and seasonality both change over time, so an association cannot isolate a causal effect of inflation. Unit sales, unmet demand, branch prices, promotions and lockdown effects are unavailable. Holiday associations require calendars.

Block 6 needs special handling for three inputs. Weather is observed after the prediction cutoff and serves as the team’s agreed proxy for historical forecast evaluation. A seasonal offer flag must come from a schedule or an independently specified rule available at prediction time. HICP breakdowns generally arrive around the middle of the following month, and the historical CSV contains no publication timestamps or original release vintages. A one-month offset can therefore use an unreleased figure at the start of a month. A two-month offset from prediction time is a conservative proxy. Historical release timestamps and vintages would establish exact availability. For the Kaggle variant, the team also needs to specify whether future external inputs are evaluated as retrospective proxies or subject to a fixed pre-test information cutoff. [Eurostat HICP release and revisions](https://ec.europa.eu/eurostat/web/hicp/information-data)

## Decisions for team confirmation

1. **Sales gaps and daily totals.** Keep observed sales as the target, or fill absent rows with zero if closures or non-offer status can be independently confirmed. Recommended: keep the 38 missing dates and 53 confectionery gaps flagged, preserve the agreed split, and state which dates qualify for complete daily-total scoring. If zero actuals are added after verification, agree how MAPE handles a zero denominator.
2. **Seasonal bread.** Use an independent offer calendar, a calendar rule defined from training and fixed before validation, or evaluate only recorded seasonal sales with a coverage caveat. Recommended: obtain the offer calendar for days where availability matters. The 292 sale rows measure recorded sales and give limited evidence on the actual offer window.
3. **Weather joins, encoding and gaps.** Left join and retain all 9,334 rows, or exclude incomplete weather dates. Recommended: retain all rows, flag the three missing weather dates, fit numeric weather imputations on training only where needed, and encode weather code as a category with a dedicated missing level. Blank codes match 2,309 sales rows, and their frequency varies by month. Keep the reported wind values pending source confirmation. Compare with a weather-free version if the team wants to measure sensitivity to observed weather as a proxy.
4. **Calendar and event joins.** Approve date joins and Kiel Week 0 outside documented event dates. For binary holiday indicators, use historical Schleswig-Holstein public holidays and mainland school holidays, or run an initial prepared dataset without those indicators. The KMK archive covers the relevant school years and distinguishes region-specific exceptions. Use historical state rules for public holidays. Retain the fixed split including its partial calendar years. Calendar weekday ordering is Monday through Sunday. [KMK school holiday archive](https://www.kmk.org/service/ferienregelung.html) · [Schleswig-Holstein historical legislation portal](https://www.gesetze-rechtsprechung.sh.juris.de/bssh/M2C2b)
5. **Inflation.** Use it as an optional predictor, additionally deflate turnover, or leave it out of modelling. Recommended: preserve nominal turnover for the agreed metrics and consider inflation as a candidate feature. Use actual publication dates and vintages if available, or approve two months back from prediction time as a proxy. Both tested lags match every sales row. An unconditional one-month offset may use data that had yet to be released.
6. **Baseline gaps.** Score direct head-to-head on rows with both predictions, or define a fallback before evaluation and score it on the full approved target set. Recommended: agree on a fallback such as the most recent same-weekday observation known at cutoff, subject to offer status, and report coverage. The exact rule has 42 missing validation predictions.
7. **Kaggle.** Provide the test file or course competition link and choose fixed-cutoff evaluation or a documented retrospective external-data variant. Recommended: fix the information available at the prediction cutoff and keep reporting distinct from next-day evaluation. The test keys and joins remain unverified.
8. **Proposed checks.** Confirm which checks below to add to canvas block 8.

### Proposed checks

- **A. Source integrity.** Unique sales date/group and ID with consistent encoding, known group codes, positive observed targets, unique daily/monthly external keys, weather bounds and one HICP record per expected month.
- **B. Join integrity.** Each left join preserves sales keys and row count. Explicit gap flags distinguish absent weather rows, blank weather values and calendar event defaults. Approved external calendars and test keys get join coverage checks.
- **C. Evaluation integrity.** Enforce the agreed split, verify approved target and daily-total coverage, align baseline and model scoring, count fallback use, and apply the agreed treatment of zero actuals.
- **D. Information cutoff.** Check that all sales features use dates before the target, availability flags use an approved source and HICP obeys the chosen cutoff. Check that training alone fits preprocessing and that the Kaggle variant uses only permitted inputs.

