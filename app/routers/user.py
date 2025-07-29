from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import UserCreate, UserOut
from app.services.user_service import UserService
from typing import List

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    pass

@router.get("/", response_model=List[UserOut])
async def list_users(db: AsyncSession = Depends(get_db)):
    pass
