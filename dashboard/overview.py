import streamlit as st
from modules.sales.sales_service import get_daily_sales

def show_overview():
    st.subheader("📈 Penjualan Harian")

    df = get_daily_sales()
    st.line_chart(df.set_index("date"))
