import streamlit as st
from modules.recipe.recipe_service import usage_per_product

def show_usage_product(start_date=None, end_date=None):
    st.subheader("🍳 Pemakaian per Produk")

    df = usage_per_product(start_date, end_date)

    st.dataframe(df)
