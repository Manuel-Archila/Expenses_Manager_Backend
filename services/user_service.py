from fastapi import APIRouter, Depends
from schemas.user_schema import CreateUserRequest, LoginRequest, TokenRefreshRequest
from managers.user_manager import UserManager
from dependencies import get_user_manager

router = APIRouter()

@router.post("/users")
def create_new_user(user: CreateUserRequest, manager: UserManager = Depends(get_user_manager)):
    return manager.create_user(user)

@router.post("/login")
def login_user(credentials: LoginRequest, manager: UserManager = Depends(get_user_manager)):
    return manager.login(credentials)

@router.post("/refresh-token")
def refresh_token(request: TokenRefreshRequest, manager: UserManager = Depends(get_user_manager)):
    return manager.refresh_access_token(request.refresh_token)