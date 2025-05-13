from dataclasses import dataclass
from datetime import date
from sqlalchemy.orm import Session
from storage.models.expense import Expense
from storage.models.user import User
from schemas.expense_schema import ExpenseCreate, ExpenseUpdate

@dataclass
class ExpenseManager:
    db: Session

    def create_expense(self, data: ExpenseCreate, user: User):
        expense = Expense(**data.model_dump())
        expense.user_id = user.id
        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return {"is_success": True, "message": "Expense created successfully", "data": expense}

    def get_user_expenses(self, user: User):
        today = date.today()
        start_of_month = today.replace(day=1)

        expenses = (
            self.db.query(Expense)
            .filter(
                Expense.user_id == user.id,
                Expense.date >= start_of_month,
                Expense.date <= today
            )
            .order_by(Expense.date.desc())
            .all()
        )
        return {"is_success": True, "message": "Expenses retrieved successfully", "data": expenses}
    
    def get_recent_expenses(self, user: User):
        recent = self.db.query(Expense).filter_by(user_id=user.id).order_by(Expense.date.desc()).limit(5).all()
        return {"is_success": True, "message": "Recent expenses retrieved successfully", "data": recent}

    def update_expense(self, expense_id: int, data: ExpenseUpdate, user: User):
        expense = self.db.query(Expense).filter_by(id=expense_id, user_id=user.id).first()
        if not expense:
            return {"is_success": False, "message": "Expense not found or unauthorized"}
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(expense, key, value)
        self.db.commit()
        self.db.refresh(expense)
        return {"is_success": True, "message": "Expense updated successfully", "data": expense}

    def delete_expense(self, expense_id: int, user: User):
        expense = self.db.query(Expense).filter_by(id=expense_id, user_id=user.id).first()
        if not expense:
            return {"is_success": False, "message": "Expense not found or unauthorized"}
        self.db.delete(expense)
        self.db.commit()
        return {"is_success": True, "message": "Expense deleted successfully", "data": None}
