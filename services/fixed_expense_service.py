from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.fixed_expense_schema import FixedExpenseCreate, FixedExpenseUpdate
from managers.fixed_expense import FixedExpenseManager
from dependencies import get_fixed_expense_manager
from storage.models.user import User
from utils.auth import get_current_user

router = APIRouter()

@router.post("/fixed-expenses")
def create_fixed_expense(
    data: FixedExpenseCreate,
    manager: FixedExpenseManager = Depends(get_fixed_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.create_fixed_expense(data, current_user)

@router.get("/fixed-expenses")
def get_fixed_expenses(
    manager: FixedExpenseManager = Depends(get_fixed_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.get_user_fixed_expenses(current_user)

@router.put("/fixed-expenses/{fixed_expense_id}")
def update_fixed_expense(
    fixed_expense_id: int,
    data: FixedExpenseUpdate,
    manager: FixedExpenseManager = Depends(get_fixed_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.update_fixed_expense(fixed_expense_id, data, current_user)

@router.delete("/fixed-expenses/{fixed_expense_id}")
def delete_fixed_expense(
    fixed_expense_id: int,
    manager: FixedExpenseManager = Depends(get_fixed_expense_manager),
    current_user: User = Depends(get_current_user)
):
    return manager.delete_fixed_expense(fixed_expense_id, current_user)
