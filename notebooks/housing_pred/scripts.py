"""Module for listing down additional custom functions required for the notebooks."""

import pandas as pd

def binned_house_value(df):
    """Bin the selling price column using quantiles."""
    return pd.qcut(df["median_house_value"], q=10)