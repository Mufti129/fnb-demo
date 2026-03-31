import streamlit as st
from modules.recipe.recipe_service import calculate_usage

def show_usage(start_date=None, end_date=None):
    st.subheader("🍳 Pemakaian Bahan")

    df = calculate_usage(start_date, end_date)
    df["total_usage"] = df["total_usage"].astype(str) + " " + df["unit"]

    st.dataframe(df)
