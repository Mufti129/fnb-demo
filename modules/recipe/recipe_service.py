from utils.gsheet_loader import load_sheet

def calculate_usage():
    sales = load_sheet("sales")
    recipe = load_sheet("recipe")

    merged = sales.merge(recipe, on="product_id")

    merged["total_usage"] = merged["qty"] * merged["ingredient_qty"]

    return merged.groupby(["ingredient_id","unit"])["total_usage"].sum().reset_index()


def usage_per_product():
    sales = load_sheet("sales")
    recipe = load_sheet("recipe")

    merged = sales.merge(recipe, on="product_id")

    merged["usage"] = merged["qty"] * merged["ingredient_qty"]

    return merged.groupby(["product_id","ingredient_id"])["usage"].sum().reset_index()
