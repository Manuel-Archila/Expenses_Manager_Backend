from dataclasses import dataclass
from sqlalchemy.orm import Session
from storage.models.category import Category
from storage.models.user import User
from schemas.category_schema import CategoryCreate

@dataclass
class CategoryManager:
    db: Session

    def create_category(self, data: CategoryCreate, user: User):
        category = Category(**data.model_dump())
        category.user_id = user.id
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return {"is_success": True, "message": "Category created successfully", "data": category}

    def get_user_categories(self, user: User):
        categories = self.db.query(Category).filter_by(user_id=user.id).all()
        return {"is_success": True, "message": "Categories retrieved successfully", "data": categories}
    
    def update_category(self, category_id: int, data: CategoryCreate, user: User):
        category = self.db.query(Category).filter_by(id=category_id, user_id=user.id).first()
        if category:
            for key, value in data.model_dump(exclude_unset=True).items():
                setattr(category, key, value)
            self.db.commit()
            self.db.refresh(category)
            return {"is_success": True, "message": "Category updated successfully", "data": {
                "id": category.id,
                "name": category.name,
                "color": category.color,
                "user_id": category.user_id
            }}
        return {"is_success": False, "message": "Category not found or unauthorized"}

    def delete_category(self, category_id: int, user: User):
        category = self.db.query(Category).filter_by(id=category_id, user_id=user.id).first()
        if category:
            self.db.delete(category)
            self.db.commit()
            return {"is_success": True, "message": "Category deleted successfully", "data": None}
        return {"is_success": False, "message": "Category not found or unauthorized", "data": None}
