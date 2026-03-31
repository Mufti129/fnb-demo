import streamlit as st
import pandas as pd
from modules.sales.sales_service import get_daily_sales

def show_overview(start_date=None, end_date=None):
    st.subheader("📈 Penjualan Harian")

    df = get_daily_sales(start_date, end_date)

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        st.line_chart(df.set_index("date"))
