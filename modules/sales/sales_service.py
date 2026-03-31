from utils.gsheet_loader import load_sheet

def get_daily_sales():
    df = load_sheet("sales")
    return df.groupby("date")["total"].sum().reset_index()

def get_sales_per_product():
    df = load_sheet("sales")

    return df.groupby("product_id").agg({
        "qty": "sum",
        "total": "sum"
    }).reset_index()
