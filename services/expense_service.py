from fastapi import APIRouter, Depends
from schemas.expense_schema import ExpenseCreate, ExpenseUpdate
from managers.expense import ExpenseManager
from dependencies import get_db
from storage.models.user import User
from utils.auth import get_current_user
from dependencies import get_expense_manager

router = APIRouter()

@router.post("/expenses")
def create_expense(
    data: ExpenseCreate,
    manager: ExpenseManager = Depends(get_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.create_expense(data, current_user)

@router.get("/expenses")
def get_expenses(
    manager: ExpenseManager = Depends(get_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.get_user_expenses(current_user)

@router.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    manager: ExpenseManager = Depends(get_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.update_expense(expense_id, data, current_user)

@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    manager: ExpenseManager = Depends(get_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.delete_expense(expense_id, current_user)

@router.get("/expenses/recent")
def get_recent_expenses(
    manager: ExpenseManager = Depends(get_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.get_recent_expenses(current_user)
