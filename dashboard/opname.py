import streamlit as st
from modules.stock.discrepancy_service import calculate_discrepancy

def show_opname():
    st.subheader("⚖️ Stock Opname & Selisih")

    df = calculate_discrepancy()

    st.dataframe(df)

    st.subheader("🚨 Alert Selisih")
    alert = df[abs(df["selisih"]) > 10]
    st.dataframe(alert)
