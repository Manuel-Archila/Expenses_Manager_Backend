from fastapi import Depends
from managers.category import CategoryManager
from managers.expense import ExpenseManager
from managers.user_manager import UserManager
from storage.database import SessionLocal
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_manager(db: Session = Depends(get_db)):
    return UserManager(db)

def get_category_manager(db: Session = Depends(get_db)):
    return CategoryManager(db)

def get_expense_manager(db: Session = Depends(get_db)):
    return ExpenseManager(db)