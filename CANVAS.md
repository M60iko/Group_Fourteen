# Agentic Data Science Canvas

**Project:** Cinnamon
**Team:** Marco, Aia, Maria, Rebecca
**Version:** 2026-11-20

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
<!-- Who decides what, when and how often? What happens today without this analysis? -->
- **Who and what:** the bakery's operations manager decides how much of each of the six product groups to bake for the next day, for one branch.
- **When:** once a day, at closing time. Today's sales are complete at that moment.
- **What the analysis delivers:** a forecast of tomorrow's turnover per product group. The operations manager converts it into baking quantities, because the data has no unit counts.
- **Seasonal bread:** forecast only on days when it is on offer.
- **Today:** decided by experience, roughly the same as on the same weekday of the previous week.
- **Scope:** the real next-day decision. The Kaggle forecast (08/2018 – 07/2019, no recent sales) is a separate evaluation variant, see block 4.

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
- **Q-a:** How much turnover will each product group have tomorrow?
- **Q-b:** Which factors known in advance shift it: weekday, public and school holidays, Kiel Week, season, weather forecast, inflation, and other external events such as lockdowns?
- **The data cannot answer:** real demand on sold-out days (turnover is what was sold); the effect of prices or promotions (not in the data); unit quantities; the effect of lockdowns or similar shocks, because the data covers 2013 – 2018 and contains none.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->
- **Operations manager:** a short daily table with tomorrow's forecast per product group, in plain words, plus one line on how reliable the forecast usually is.
- **Technical reader:** a data team taking over the repository; READMEs and notebooks reproduce every result.
- **Course:** final presentation with the MAPE per product group.

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->
- **Metrics:** MAPE and the mean absolute error in turnover (MAE), each per product group and for the daily total of all groups. Always reported on validation data, next to the training score.
- **Baseline to beat:** same weekday of the previous week (current practice).
- **Good enough:** the model must beat the baseline at least on the daily total of all groups. The goal is to beat it in every product group; groups where it does not are reported openly.
- **Costly errors:** baking too much and too little are treated as equally bad for now, because there is no cost data. Open question for the client.
- **Split:** training 01.07.2013 – 31.07.2017, validation 01.08.2017 – 31.07.2018, test = Kaggle file. No training date after the start of validation.
- **Variants:** the next-day forecast is the main evaluation. The Kaggle forecast is evaluated separately, without recent sales.

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->
- **Inflation (additional source):** Eurostat HICP for Germany, monthly, 01/2012 – 07/2019, all items and bread and cereals. See `0_DataPreparation/inflation_germany.ipynb`. Changes slowly, so over five years it acts mostly like a trend.

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
- **Moment of prediction:** closing time of the day before.
- **Known:** sales of all groups up to and including today; tomorrow's calendar (weekday, month, public holidays, school holidays, Kiel Week); whether seasonal bread is on offer; tomorrow's weather forecast; inflation of an earlier month (the current month is not yet published; proposed delay: 1 month, to be confirmed).
- **Stand-in:** the data only has observed weather, used as a stand-in for the forecast. This is slightly optimistic and must be named as a limit.
- **Not known (leakage):** tomorrow's sales of any group, and anything computed from them (unshifted rolling means, totals that include tomorrow).
- **Kaggle variant:** no sales after 31.07.2018 are known, so recent sales cannot be features.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- Which error costs more: baking too much or too little? (client, via the team)
- Lockdowns and similar shocks: the data contains none, so the model cannot know their effect. How should the forecast be used in such periods? (team, with the client)
- Public and school holidays are not in the dataset: which source do we use? (team, before /explore-data)
- Who in the team is responsible for which part? (team)
- Inflation: which delay (1 month proposed), and is it used as a feature, to convert turnover into real turnover, or both? (team)

## Decision log
See `DECISIONS.md`.
