import streamlit as st
from modules.stock.stock_service import get_real_stock

def show_stock():
    st.subheader("📦 Stok Real")

    df = get_real_stock()
    df["stok_real"] = df["stok_real"].astype(str) + " " + df["unit"]

    st.dataframe(df)
