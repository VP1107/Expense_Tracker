from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

import schemas
import models
from dependencies import get_db, get_current_user

router = APIRouter(prefix="/expenses", tags=["expenses"])

# Create Expense
@router.post("", response_model=schemas.ExpenseOut)
def create_expense(expense: schemas.ExpenseCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_expense = models.Expense(
        user_id = current_user.id,
        name = expense.name,
        amount = expense.amount,
        category = expense.category,
        description = expense.description
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.get("", response_model=list[schemas.ExpenseOut])
def get_expenses(
    category: str | None = None,
    name: str | None = None,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(models.Expense).filter(models.Expense.user_id == current_user.id)
    if category:
        query = query.filter(models.Expense.category == category)
    if name:
        query = query.filter(models.Expense.name == name)
    return query.all()


@router.get("/{expense_id}", response_model=schemas.ExpenseOut)
def get_expense(expense_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id,
        models.Expense.user_id == current_user.id
    ).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


# Update Expense
@router.patch("/{expense_id}", response_model=schemas.ExpenseOut)
def update_expense(expense_id: int, expense_update: schemas.ExpenseUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.user_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    for field, value in expense_update.model_dump(exclude_unset=True).items():
        setattr(expense, field, value)

    db.commit()
    db.refresh(expense)
    return expense


# Delete Expense
@router.delete("/{expense_id}", status_code=204)
def delete_expense(expense_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.user_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()