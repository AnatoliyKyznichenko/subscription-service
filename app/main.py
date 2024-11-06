from fastapi import FastAPI
from app.api.routes import users, subscriptions
import uvicorn

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(subscriptions.router, prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)