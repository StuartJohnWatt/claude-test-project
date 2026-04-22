import polars as pl
from pathlib import Path

DATA_PATH = Path("/data/sales.csv")


def load_data() -> pl.DataFrame:
    return pl.read_csv(DATA_PATH, try_parse_dates=True)


def summary_by_category(df: pl.DataFrame) -> list[dict]:
    return (
        df.group_by("category")
        .agg(
            pl.col("units_sold").sum().alias("total_units"),
            pl.col("revenue").sum().round(2).alias("total_revenue"),
        )
        .sort("total_revenue", descending=True)
        .to_dicts()
    )


def monthly_revenue(df: pl.DataFrame) -> list[dict]:
    return (
        df.with_columns(pl.col("date").dt.strftime("%Y-%m").alias("month"))
        .group_by("month")
        .agg(pl.col("revenue").sum().round(2).alias("total_revenue"))
        .sort("month")
        .to_dicts()
    )
