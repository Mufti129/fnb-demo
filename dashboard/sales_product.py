import streamlit as st
from modules.sales.sales_service import get_sales_per_product

def show_sales_product():
    st.subheader("📊 Penjualan per Produk")

    df = get_sales_per_product()

    df["total"] = df["total"].apply(lambda x: f"Rp {x:,.0f}")

    st.dataframe(df)
