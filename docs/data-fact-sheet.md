# Data fact sheet

Profile of the three course datasets (`/explore-data`, step 1), computed on 2026-11-23 from the files in the course repository. Numbers are from running the code, not from the README. Draft by Rebecca's agent: data decisions below are **open for the team**.

## Sources

| Source | Rows | One row is | Period | Key | Unique? |
|---|---|---|---|---|---|
| `umsatzdaten_gekuerzt.csv` (sales) | 9,334 | one date × product group | 01.07.2013 – 31.07.2018 | `Datum` + `Warengruppe` (= `id`) | yes, 0 duplicates; `id` matches `YYMMDD` + group in every row |
| `wetter.csv` (weather) | 2,601 | one date | 01.01.2012 – 01.08.2019 | `Datum` | yes |
| `kiwo.csv` (Kiel Week) | 72 | one Kiel Week day | 16.06.2012 – 30.06.2019 | `Datum` | yes |

Origin: meteolytix GmbH via the opencampus.sh course repository. License: not stated.

## Sales

- 1,857 calendar days in the period, 1,819 with sales, **38 days without any sales** (mostly 25/26 Dec, 1 Jan, Good Friday, 1 May; also e.g. 2014-05-03/04, 2016-07-07, 2017-07-04, 2017-10-23).
- No missing values in the columns. Turnover 7.05 – 1,879.46, median 161.9.

| Group | Days | Mean | Median | SD | Min | Max |
|---|---|---|---|---|---|---|
| 1 Bread | 1,819 | 122.1 | 120.1 | 40.3 | 23.1 | 416.8 |
| 2 Rolls | 1,819 | 402.5 | 370.8 | 139.7 | 175.0 | 1,203.4 |
| 3 Croissants | 1,819 | 163.3 | 142.8 | 75.6 | 37.7 | 565.9 |
| 4 Confectionery | 1,766 | 88.0 | 80.0 | 35.3 | 27.4 | 430.5 |
| 5 Cakes | 1,819 | 276.8 | 266.0 | 99.5 | 121.5 | 1,879.5 |
| 6 Seasonal bread | 292 | 66.9 | 62.9 | 32.4 | 7.1 | 172.9 |

- **Group 4 is missing on 53 sales days**, all in 2013 – 2016 (2013: 16, 2014: 23, 2015: 10, 2016: 4). Missingness depends on time.
- **Group 6** sold only Oct (13 days), Nov (140), Dec (133), Jan (6).
- Cakes max 1,879 is far above the rest of the group (check: special day, e.g. New Year's Eve?).

## Weather

- 3 sales days have **no weather row**: 2016-12-11, 2017-10-04, 2017-10-05 (16 sales rows).
- Within the sales period (1,854 weather days): `Bewoelkung` missing on 10 days, `Wettercode` missing on 463 days (669 in the whole file).
- **Missing `Wettercode` is not random:** on those days cloud cover is lower (2.9 vs 5.3 octas) and it is warmer (16.1 vs 10.8 °C). This supports the README's reading "no notable weather".
- Temperature −10.3 to 32.7 °C. **`Windgeschwindigkeit` 3 – 35, mean 11.2:** the README says m/s, but a daily mean of 35 m/s would be a hurricane; the unit is probably km/h or knots. To check.

## Kiel Week

- 45 Kiel Week days fall into the sales period; all 45 match a sales day.

## Joins (left join on `Datum`, sales as the left table)

- Sales → weather: 9,318 rows matched, 16 without weather, 0 rows added. Row count stays 9,334.
- Sales → Kiel Week: 45 dates matched; all other days get `KielerWoche = 0`.

## Open data decisions (for the team, canvas block 7)

1. **Days without any sales (38):** leave out (recommended: they are closing days and need no forecast) or add as 0?
2. **Group 4 missing on 53 days:** treat as "not on offer" and leave out (recommended), or fill with 0?
3. **Seasonal bread:** only model on days with sales (matches the decision in block 1).
4. **Missing weather (3 days):** interpolate from neighbouring days (recommended) or drop those rows?
5. **Missing `Wettercode`:** own category "no notable weather" (recommended, missingness is informative) or drop the column?
6. **Wind speed unit:** clarify before using it as a feature.
7. **Outliers (e.g. cakes 1,879):** keep and flag special days, or cap?
8. **Public and school holidays:** not in the data; source still open (see canvas).

## Candidate checks (for canvas block 8)

- Merged data has exactly 9,334 rows; one row per `Datum` × `Warengruppe`.
- No duplicated dates in weather and Kiel Week.
- `KielerWoche` is 0 or 1, no missing values after the merge.
- Every training date ≤ 31.07.2017, every validation date in 01.08.2017 – 31.07.2018.
