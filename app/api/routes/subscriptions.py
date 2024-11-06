from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.subscription import SubscriptionResponse, SubscriptionCreate
from app.services.subscriptions_service import get_active_subscription, create_subscription

router = APIRouter()


@router.post("/subscriptions/create", response_model=SubscriptionResponse)
async def create_user_subscription(user_id: int, subscription_data: SubscriptionCreate,
                                   db: AsyncSession = Depends(get_db)):
    active_subscription = await get_active_subscription(db, user_id=user_id)
    if active_subscription:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already has an active subscription")

    new_subscription = await create_subscription(db, user_id, subscription_data)
    return new_subscription


@router.get("/subscriptions/active", response_model=SubscriptionResponse)
async def get_user_active_subscription(user_id: int, db: AsyncSession = Depends(get_db)):
    active_subscription = await get_active_subscription(db, user_id=user_id)
    if not active_subscription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active subscription found")

    return active_subscription
