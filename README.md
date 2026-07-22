# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.
  
# 🚀 Project Overview

The Expense Management System allows users to:

- Add daily expenses
- Update existing expenses
- Delete expenses by date
- Retrieve expenses for a specific date
- Analyze expenses by category
- Analyze monthly spending trends
- View expense summaries using charts and tables

The backend exposes APIs using FastAPI, while the Streamlit frontend consumes these APIs to provide a user-friendly dashboard.

---

✨ Features

## Expense Management

✅ Add new expenses  
✅ Update existing expenses  
✅ Delete expenses for a selected date  
✅ Fetch expenses based on date  
✅ Store expense details in MySQL database  

Expense fields:

- Date
- Amount
- Category
- Notes

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```

   ## Analytics Dashboard

### Category Analysis

- Total spending by category
- Percentage contribution of each category
- Category-wise expense visualization


### Monthly Analysis

- Monthly expense summary
- Month-wise spending trends
- Bar chart visualization


## Backend Features

- REST API development using FastAPI
- MySQL database integration
- CRUD operations
- Data validation using Pydantic
- API error handling
- Logging implementation
- Automated testing using Pytest


## Frontend Features

- Interactive Streamlit UI
- Date-based expense filtering
- Expense update form
- Analytics dashboard
- Data visualization

---

# 🛠️ Tech Stack

## Backend

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- MySQL Connector


## Frontend

- Streamlit
- Requests
- Pandas


## Database

- MySQL


## Testing

- Pytest


## Development Tools

- Git & GitHub
- VS Code
- Postman

---
# 📸 Screenshots

## Expense Dashboard

![Expense Dashboard](C:\Users\samru\OneDrive\Pictures\Screenshots\Screenshot Expense_Management_Sysytem.png)


## Category Analysis

![Category Analysis](screenshots/category_analysis.png)


## Monthly Analysis

![Monthly Analysis](screenshots/monthly_analysis.png)
