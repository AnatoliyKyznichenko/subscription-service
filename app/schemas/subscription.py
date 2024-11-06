from pydantic import BaseModel
from datetime import datetime


class SubscriptionCreate(BaseModel):
    plan_name: str
    end_date: datetime
    price: float

class SubscriptionResponse(BaseModel):
    id: int
    plan_name: str
    start_date: datetime
    end_date: datetime
    status: str
    price: float

    class Config:
        from_attributes = True