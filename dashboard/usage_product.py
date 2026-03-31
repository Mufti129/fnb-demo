import streamlit as st
from modules.recipe.recipe_service import usage_per_product

def show_usage_product():
    st.subheader("🍳 Pemakaian Bahan per Produk")

    df = usage_per_product()

    st.dataframe(df)
