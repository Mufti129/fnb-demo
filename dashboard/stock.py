import streamlit as st
from modules.stock.stock_service import get_real_stock


def show_stock(stock_date=None):
    st.subheader("📦 Stok Real (Snapshot)")

    df = get_real_stock(stock_date)
    df["stok_real"] = df["stok_real"].astype(str) + " " + df["unit"]

    st.dataframe(df)
