import pandas as pd
import streamlit as st
from config.gsheet_config import connect_gsheet

SPREADSHEET_ID = "13wQcCXIYRb__HO-Vb0Zm_f77u9628uKt4YDgD94IpiY"

@st.cache_data
def load_sheet(sheet_name):
    client = connect_gsheet()

    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    sheet = spreadsheet.worksheet(sheet_name)

    data = sheet.get_all_records()

    return pd.DataFrame(data)
