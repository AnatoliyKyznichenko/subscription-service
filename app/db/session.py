from sqlalchemy.ext.asyncio import (create_async_engine,
                                    AsyncSession,
                                 async_sessionmaker)

from app.core.config import settings

async_engine = create_async_engine(settings.DB_PATH, echo=False)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

