import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")

    if response.status_code != 200:
        st.error(f"API Error: {response.status_code}")
        st.write(response.text)
        return

    monthly_summary = response.json()

    df = pd.DataFrame(monthly_summary)

    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    df_sorted = df.sort_values(by="Month Number")
    df_sorted.set_index("Month Number", inplace=True)

    st.title("Expense Breakdown By Months")

    # ✅ No width or height arguments
    st.bar_chart(
        df_sorted.set_index("Month Name")["Total"],
        use_container_width=True
    )

    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted.sort_index())