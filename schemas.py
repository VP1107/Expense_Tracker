from pydantic import BaseModel, ConfigDict, EmailStr, Field
from decimal import Decimal
from datetime import datetime


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr


class UserCredentials(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class MessageResponse(BaseModel):
    message: str
    user_id: int | None = None  # optional — delete endpoints return no user_id


class ExpenseCreate(BaseModel):
    name: str = Field(max_length=50)
    amount: Decimal = Field(gt=0, decimal_places=2)
    category: str = Field(max_length=100)
    description: str | None = None  # optional, not everyone adds a description
    # Remove user_id — it comes from the token, not the request body


class ExpenseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    name: str
    amount: Decimal  # match the Numeric(10,2) column
    category: str
    description: str | None  # nullable in DB, must be Optional here
    created_at: datetime  # you have this column, expose it


class ExpenseUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=50)
    amount: Decimal | None = Field(default=None, gt=0, decimal_places=2)
    category: str | None = Field(default=None, max_length=100)
    description: str | None = None