import pandas as pd
import streamlit as st
from config.gsheet_config import connect_gsheet

@st.cache_data
def load_sheet(sheet_name):
    client = connect_gsheet()
    sheet = client.open("FNB_DATABASE").worksheet(sheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)
