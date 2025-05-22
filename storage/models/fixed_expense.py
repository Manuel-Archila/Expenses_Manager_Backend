from sqlalchemy import Column, Date, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from storage.database import Base

class FixedExpense(Base):
    __tablename__ = "fixed_expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric, nullable=False)
    description = Column(String)
    frequency = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    payment_date = Column(Date, nullable=True)
    notify = Column(String, nullable=True)

    user = relationship("User", back_populates="fixed_expenses")
    category = relationship("Category", back_populates="fixed_expenses")
