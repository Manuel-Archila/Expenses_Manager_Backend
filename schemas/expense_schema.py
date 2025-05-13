from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float
    description: Optional[str] = None
    date: date
    category_id: int

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date_created: Optional[date] = None
    category_id: Optional[int] = None
