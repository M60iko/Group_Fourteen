"""First check: the raw sales data can be loaded and looks as documented.

Run all checks with: uv run pytest checks
This check needs an internet connection, because the data is loaded from GitHub.
"""

import pandas as pd

SALES_URL = (
    "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/"
    "main/data/bakery/umsatzdaten_gekuerzt.csv"
)


def test_sales_data_loads():
    sales = pd.read_csv(SALES_URL, parse_dates=["Datum"])

    # The dataset documentation states 9,334 rows, one per date and product group.
    assert len(sales) == 9334
    assert {"id", "Datum", "Warengruppe", "Umsatz"} <= set(sales.columns)
    assert not sales.duplicated(subset=["Datum", "Warengruppe"]).any()
