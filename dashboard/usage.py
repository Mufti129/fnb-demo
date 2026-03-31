import streamlit as st
from modules.recipe.recipe_service import calculate_usage

def show_usage():
    st.subheader("🍳 Pemakaian Bahan")

    df = calculate_usage()
    df["total_usage"] = df["total_usage"].astype(str) + " " + df["unit"]

    st.dataframe(df)
