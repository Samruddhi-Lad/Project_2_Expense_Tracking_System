import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"


def add_update_tab(selected_date):
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    existing_expenses = []

    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}")

        if response.status_code == 200:
            existing_expenses = response.json()
        else:
            st.error("Failed to retrieve expenses")
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form("expense_form"):

        col1, col2, col3 = st.columns(3)
        col1.write("Amount")
        col2.write("Category")
        col3.write("Notes")

        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                selected_cat = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                selected_cat = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)

            with col1:
                st.number_input(
                    "Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                st.selectbox(
                    "Category",
                    options=categories,
                    index=categories.index(selected_cat),
                    key=f"category_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                st.text_input(
                    "Notes",
                    value=notes,
                    key=f"notes_{selected_date}_{i}",
                    label_visibility="collapsed"
                )

        submit_button = st.form_submit_button("Save")

        if submit_button:
            st.success("Ready to save expenses.")