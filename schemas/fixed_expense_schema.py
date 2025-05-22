from pydantic import BaseModel
from typing import Optional
from datetime import date

class FixedExpenseCreate(BaseModel):
    amount: float
    description: Optional[str] = None
    frequency: str
    category_id: int
    payment_date: Optional[date] = None
    notify: Optional[bool] = None

class FixedExpenseUpdate(BaseModel):
    amount: float
    description: Optional[str] = None
    frequency: str
    category_id: int
    payment_date: Optional[date] = None
    notify: Optional[bool] = None
