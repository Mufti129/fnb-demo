from utils.gsheet_loader import load_sheet
from modules.stock.stock_service import get_real_stock

def calculate_discrepancy():
    system_stock = get_real_stock()
    opname = load_sheet("stock_opname")

    opname_latest = opname.sort_values("date").groupby("ingredient_id").last().reset_index()

    merged = system_stock.merge(opname_latest, on="ingredient_id", how="left")
    merged["real_qty"] = merged["real_qty"].fillna(0)

    merged["selisih"] = merged["real_qty"] - merged["stok_real"]

    return merged
