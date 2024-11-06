from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.db.base import Base

if TYPE_CHECKING: # Избегаем циклического импорта / сли только идет проверка типов а не выполнения кода
    from app.models.user import User

class Subscription(Base):
    __tablename__ = 'subscription'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    plan_name: Mapped[str] = mapped_column(String, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    end_date: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String, default='active')
    price: Mapped[float] = mapped_column(Float)

    user: Mapped['User'] = relationship('User', back_populates='subscription')
