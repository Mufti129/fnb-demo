import pandas as pd
from utils.gsheet_loader import load_sheet

def get_all_stock():
    g1 = load_sheet("stock_gudang_1")
    g2 = load_sheet("stock_gudang_2")

    stock = pd.concat([g1, g2])
    return stock.groupby(["ingredient_id","unit"])["qty"].sum().reset_index()


def get_real_stock():
    from modules.recipe.recipe_service import calculate_usage

    stock = get_all_stock()
    usage = calculate_usage()

    merged = stock.merge(usage, on=["ingredient_id","unit"], how="left")
    merged["total_usage"] = merged["total_usage"].fillna(0)

    merged["stok_real"] = merged["qty"] - merged["total_usage"]

    return merged
