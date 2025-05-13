from dataclasses import dataclass
import os
from fastapi import HTTPException
import jwt
from sqlalchemy.orm import Session
from storage.models.user import User
from schemas.user_schema import CreateUserRequest, LoginRequest
from utils.jwt import create_access_token, create_refresh_token
from utils.security import hash_password, verify_password

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

@dataclass
class UserManager:
    db: Session

    def create_user(self, user_data: CreateUserRequest):
        try:
            existing_user = self.db.query(User).filter(User.email == user_data.email).first()
            if existing_user:
                return {
                    "is_success": False,
                    "message": "User with this email already exists.",
                    "data": None
                }
            hashed_pwd = hash_password(user_data.password)
            user = User(
                name=user_data.name,
                email=user_data.email,
                password=hashed_pwd
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return {
                "is_success": True,
                "message": "User created successfully.",
                "data": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                }
            }
        except Exception as e:
            self.db.rollback()
            return {
                "is_success": False,
                "message": str(e),
                "data": None
            }
    
    def login(self, credentials: LoginRequest):
        try:
            user = self.db.query(User).filter(User.email == credentials.email).first()
            if not user:
                raise HTTPException(status_code=401, detail="Credenciales inválidas")
            if not verify_password(credentials.password, user.password):
                raise HTTPException(status_code=401, detail="Credenciales inválidas")

            access_token = create_access_token({"sub": str(user.id)})
            refresh_token = create_refresh_token({"sub": str(user.id)})

            user.refresh_token = refresh_token
            self.db.commit()

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        except Exception as e:
            self.db.rollback()
            return {
                "is_success": False,
                "message": str(e),
                "data": None
            }
    
    def refresh_access_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = int(payload.get("sub"))
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Refresh token expirado")
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail="Token inválido")

        user = self.db.query(User).filter_by(id=user_id).first()
        if not user or user.refresh_token != token:
            raise HTTPException(status_code=401, detail="Refresh token inválido o no coincide")

        new_access_token = create_access_token({"sub": str(user.id)})
        new_refresh_token = create_refresh_token({"sub": str(user.id)})

        user.refresh_token = new_refresh_token
        self.db.commit()

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer"
    }
