from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.db import models

class UserService:
    @staticmethod
    async def create_user(db: AsyncSession, user_in: UserCreate):
        pass

    @staticmethod
    async def get_all_users(db: AsyncSession):
        pass
