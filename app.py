import streamlit as st

from dashboard.overview import show_overview
from dashboard.stock import show_stock
from dashboard.usage import show_usage
from dashboard.opname import show_opname
from dashboard.sales_product import show_sales_product
from dashboard.usage_product import show_usage_product
from utils.gsheet_loader import load_sheet

st.set_page_config(layout="wide")

st.title("📊 F&B Control Dashboard")

menu = st.sidebar.selectbox("Menu", [
    "Overview",
    "Stock",
    "Usage",
    "Stock Opname",
    "Sales per Product",
    "Usage per Product"
])

if menu == "Overview":
    show_overview()

elif menu == "Stock":
    show_stock()

elif menu == "Usage":
    show_usage()

elif menu == "Stock Opname":
    show_opname()

elif menu == "Sales per Product":
    show_sales_product()

elif menu == "Usage per Product":
    show_usage_product()
st.title("📊 F&B Control Dashboard")

# TEST GOOGLE SHEET
st.subheader("🧪 Test Load Sheet")
st.write(load_sheet("pricing"))
