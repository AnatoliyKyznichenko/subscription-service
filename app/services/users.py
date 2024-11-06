from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.security import hash_password, verify_password
from app.schemas.user import UserCreate
from app.models.user import User
from sqlalchemy.future import select

async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_password = hash_password(user_data.password)
    new_user = User(email=user_data.email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.password):  # Здесь SQLAlchemy должно корректно передать значение `user.password`
        return user

    return None
