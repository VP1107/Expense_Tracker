# Spendr — Expense Tracker

**Spendr** is a simple, sleek, and efficient Expense Tracker web application built with a **FastAPI** backend and a responsive vanilla HTML/CSS/JS **frontend**.

## Live Links

- **Frontend Application**: [https://spendr-ouyp.onrender.com](https://spendr-ouyp.onrender.com)
- **Backend API**: [https://spendr-backend-1e95.onrender.com](https://spendr-backend-1e95.onrender.com)

## Features

- **User Authentication**: Secure sign up and log in functionality using bcrypt.
- **Manage Expenses**: Add, view, edit, and delete expenses through an intuitive UI. Tracks currency in INR (₹).
- **Categorization & Descriptions**: Keep your expenses categorized with detailed descriptions. Includes dynamic filtering by name and category.
- **Interactive Dashboard**: A sleek sidebar displays total spent, total count, and a dynamic breakdown of expenses by category.
- **Secure**: Features token-based authentication (JWT) and modern security practices for storing passwords.
- **User-Specific Data**: Each user has their own secluded expenses workspace.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (managed with SQLAlchemy ORM)
- **Frontend**: HTML, CSS, Vanilla JavaScript

## Project Structure

```text
Expense_Tracker/
├── main.py              # Main FastAPI application entry point
├── database.py          # Database connection setup
├── models.py            # SQLAlchemy database models (User, Expense)
├── schemas.py           # Pydantic schemas for request/response validation
├── auth.py              # Authentication utilities (hashing, verify)
├── dependencies.py      # Dependency injection (e.g., get_current_user)
├── routers/             # API Router endpoints
│   ├── expenses.py      # Routes for managing expenses
│   └── user.py          # Routes for user registration and authentication
├── frontend/            # Frontend application
│   └── index.html       # The single-page frontend interface
├── requirements.txt     # Python dependencies
├── start.sh             # Startup script for production environment
└── .env                 # Environment variables for secret keys
```

## Setup & Installation

### 1. Backend Setup

1. Open a terminal and navigate to the project root directory.
2. Initialize and activate a virtual environment (already set to `myenv` locally):
   ```bash
   python -m venv myenv
   
   # On Windows:
   myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in the `.env` file for database URI and Secret Keys.
5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   *The backend will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000) and API documentation will be automatically generated at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).*

### 2. Frontend Setup

The backend has CORS explicitly configured to accept requests from `http://localhost:3000`.

1. To run the frontend correctly, navigate to the `frontend/` directory and use a local development server on port 3000.
2. **Recommended Method (VS Code):** Install the **Live Server** extension, open `frontend/index.html`, right-click on the code, and select **Open with Live Server**. Ensure that the Live Server is configured to use port `3000`.
3. You can now use the application in your browser!
