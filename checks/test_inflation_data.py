"""Checks for the inflation data (created by 0_DataPreparation/inflation_germany.ipynb).

Run all checks with: uv run pytest checks
"""

from pathlib import Path

import pandas as pd

INFLATION_FILE = Path(__file__).parent.parent / "0_DataPreparation" / "inflation_germany_monthly.csv"


def load_inflation():
    inflation = pd.read_csv(INFLATION_FILE)
    inflation["month"] = pd.PeriodIndex(inflation["month"], freq="M")
    return inflation


def test_every_month_once_without_gaps():
    inflation = load_inflation()
    expected = pd.period_range("2012-01", "2019-07", freq="M")
    assert list(inflation["month"]) == list(expected)


def test_no_missing_index_values():
    inflation = load_inflation()
    assert inflation[["hicp_all_items", "hicp_bread_cereals"]].notna().all().all()


def test_inflation_rates_from_2013_on():
    # The year-on-year rate needs the value of 12 months earlier, so it starts in 01/2013.
    inflation = load_inflation()
    from_2013 = inflation[inflation["month"] >= pd.Period("2013-01", freq="M")]
    assert from_2013[["inflation_all_items_pct", "inflation_bread_cereals_pct"]].notna().all().all()
