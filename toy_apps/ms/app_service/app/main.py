from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db import get_session, init_db
from app.models import User, UserCreate
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/users", response_model=List[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [User(email=user.email, password=user.password, id=user.id) for user in users]


@app.post("/users")
async def add_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(email=user.email, password=user.password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@app.post("/login")
async def login(login_user: UserCreate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    login_user_dict = login_user.dict()
    all_users = [{"email":user.email, "password":user.password} for user in users]
    is_valid = login_user_dict in all_users
    if is_valid:
        return {"message": "User logged in successfully"}
    else:
        return {"message": "User not found"}
