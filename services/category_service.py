from fastapi import APIRouter, Depends
from schemas.category_schema import CategoryCreate, CategoryUpdate
from managers.category import CategoryManager
from dependencies import get_category_manager
from storage.models.user import User
from utils.auth import get_current_user

router = APIRouter()


@router.post("/categories")
def create_category(category: CategoryCreate, manager: CategoryManager = Depends(get_category_manager), current_user: User = Depends(get_current_user)):
    return manager.create_category(category, current_user)

@router.get("/categories")
def get_categories(manager: CategoryManager = Depends(get_category_manager), current_user: User = Depends(get_current_user)):
    return manager.get_user_categories(current_user)

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, manager: CategoryManager = Depends(get_category_manager), current_user: User = Depends(get_current_user)):
    return manager.delete_category(category_id, current_user)

@router.put("/categories/{category_id}")
def update_category(category_id: int, category: CategoryUpdate, manager: CategoryManager = Depends(get_category_manager), current_user: User = Depends(get_current_user)):
    return manager.update_category(category_id, category, current_user)
    
