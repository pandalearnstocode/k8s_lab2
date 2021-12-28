from fastapi import Depends, FastAPI
from app.utils import generate_fake_dataframe,pandas_to_sql
# from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
# from typing import List
from app.db import get_session, init_db
# from app.models import User, UserCreate

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/generate_data/{country}")
async def foo_generate_data(country: str):
    df = generate_fake_dataframe(
    size = 30, 
    cols = "cicffcd", 
    col_names = ["user", "age", "residence", "weight","height", "pet", "registered"],
    intervals = [("names",15), (18,25),("cities", 15), (73.2,95.0),
                (1.65,1.95), ("animals", 11), None],
    seed = None)
    df['country'] = country
    pandas_to_sql(dburi="postgresql://postgres@localhost/dwd", df = df)
    return {"Message": "Data generated"}


# @app.get("/pull_data/{country}")
# async def foo_pull_data(session: AsyncSession = Depends(get_session)):
    # result = await session.execute(select(User))
    # users = result.scalars().all()
    # return [User(email=user.email, password=user.password, id=user.id) for user in users]