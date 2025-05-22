from dataclasses import dataclass
from sqlalchemy.orm import Session
from storage.models.fixed_expense import FixedExpense
from storage.models.user import User
from schemas.fixed_expense_schema import FixedExpenseCreate, FixedExpenseUpdate

@dataclass
class FixedExpenseManager:
    db: Session

    def create_fixed_expense(self, data: FixedExpenseCreate, user: User):
        item = FixedExpense(**data.model_dump())
        item.user_id = user.id
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return {"is_success": True, "message": "Fixed expense created", "data": item}

    def get_user_fixed_expenses(self, user: User):
        items = self.db.query(FixedExpense).filter_by(user_id=user.id).all()
        return {"is_success": True, "message": "Fixed expenses retrieved", "data": items}

    def update_fixed_expense(self, fixed_expense_id: int, data: FixedExpenseUpdate, user: User):
        item = self.db.query(FixedExpense).filter_by(id=fixed_expense_id, user_id=user.id).first()
        if not item:
            return {"is_success": False, "message": "Fixed expense not found or unauthorized"}
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        return {"is_success": True, "message": "Fixed expense updated", "data": item}

    def delete_fixed_expense(self, fixed_expense_id: int, user: User):
        item = self.db.query(FixedExpense).filter_by(id=fixed_expense_id, user_id=user.id).first()
        if not item:
            return {"is_success": False, "message": "Fixed expense not found or unauthorized"}
        self.db.delete(item)
        self.db.commit()
        return {"is_success": True, "message": "Fixed expense deleted"}
