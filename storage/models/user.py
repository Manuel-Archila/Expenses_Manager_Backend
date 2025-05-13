from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from storage.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)

    categories = relationship("Category", back_populates="user")
    expenses = relationship("Expense", back_populates="user")
    fixed_expenses = relationship("FixedExpense", back_populates="user")
