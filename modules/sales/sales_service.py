from utils.gsheet_loader import load_sheet
import pandas as pd

def get_daily_sales(start_date=None, end_date=None):
    df = load_sheet("sales")
    df["date"] = pd.to_datetime(df["date"])

    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    return df.groupby("date")["total"].sum().reset_index()


def get_sales_per_product(start_date=None, end_date=None):
    df = load_sheet("sales")
    df["date"] = pd.to_datetime(df["date"])

    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    return df.groupby("product_id").agg({
        "qty": "sum",
        "total": "sum"
    }).reset_index()
