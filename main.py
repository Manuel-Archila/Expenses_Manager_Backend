from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import user_service, category_service, expense_service
from storage.models import user, category, expense, fixed_expense
from storage.database import Base, engine




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


app.include_router(user_service.router)
app.include_router(category_service.router)
app.include_router(expense_service.router)
