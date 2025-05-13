from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from storage.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="categories", )
    expenses = relationship("Expense", back_populates="category", passive_deletes=True)
    fixed_expenses = relationship("FixedExpense", back_populates="category", passive_deletes=True)
