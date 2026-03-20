from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import expenses, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(expenses.router)