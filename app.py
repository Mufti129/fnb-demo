import streamlit as st
import pandas as pd

from dashboard.overview import show_overview
from dashboard.stock import show_stock
from dashboard.usage import show_usage
from dashboard.opname import show_opname
from dashboard.sales_product import show_sales_product
from dashboard.usage_product import show_usage_product

st.set_page_config(layout="wide")
st.title("📊 F&B Control Dashboard")

# 🔥 FILTER GLOBAL
st.sidebar.subheader("📅 Filter")

date_range = st.sidebar.date_input("Range Penjualan", [])
stock_date = st.sidebar.date_input("Stok per Tanggal")

start_date, end_date = None, None

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

menu = st.sidebar.selectbox("Menu", [
    "Overview",
    "Stock",
    "Usage",
    "Stock Opname",
    "Sales per Product",
    "Usage per Product"
])

if menu == "Overview":
    show_overview(start_date, end_date)

elif menu == "Stock":
    show_stock(stock_date)

elif menu == "Usage":
    show_usage(start_date, end_date)

elif menu == "Stock Opname":
    show_opname()

elif menu == "Sales per Product":
    show_sales_product(start_date, end_date)

elif menu == "Usage per Product":
    show_usage_product(start_date, end_date)
