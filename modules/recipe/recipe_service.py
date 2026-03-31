from utils.gsheet_loader import load_sheet
import pandas as pd

def calculate_usage(start_date=None, end_date=None):
    sales = load_sheet("sales")
    recipe = load_sheet("recipe")

    sales["date"] = pd.to_datetime(sales["date"])

    if start_date:
        start_date = pd.to_datetime(start_date)
        sales = sales[sales["date"] >= start_date]

    if end_date:
        end_date = pd.to_datetime(end_date)
        sales = sales[sales["date"] <= end_date]

    merged = sales.merge(recipe, on="product_id")
    merged["total_usage"] = merged["qty"] * merged["ingredient_qty"]

    return merged.groupby(["ingredient_id","unit"])["total_usage"].sum().reset_index()
