from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.subscriptions import Subscription
from app.schemas.subscription import SubscriptionCreate


async def create_subscription(db: AsyncSession, user_id: int, subscription_data: SubscriptionCreate) -> Subscription:
    subscription = Subscription(
        user_id=user_id,
        plan_name=subscription_data.plan_name,
        start_date=datetime.utcnow(),
        end_date=subscription_data.end_date,
        status="active",
        price=subscription_data.price
    )
    db.add(subscription)
    await db.commit()
    await db.refresh(subscription)
    return subscription


async def get_active_subscription(db: AsyncSession, user_id: int) -> Optional[Subscription]:
    result = await db.execute(
        select(Subscription)
        .where(Subscription.user_id == user_id, Subscription.status == "active")
    )
    return result.scalars().first()