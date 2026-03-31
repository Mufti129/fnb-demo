import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_gsheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_dict = st.secrets["gcp_service_account"]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    return gspread.authorize(creds)
