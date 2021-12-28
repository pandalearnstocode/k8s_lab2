from fastapi import FastAPI
from app.utils import generate_fake_dataframe, pandas_to_sql
import os
import pandas as pd
import psycopg2 as pg


DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_USER_NAME= os.environ.get("DATABASE_USER_NAME")
DATABASE_PASSWORD= os.environ.get("DATABASE_PASSWORD")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
# from typing import List

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
    pandas_to_sql(dburi=DATABASE_URL, df = df, table_name=country)
    return {"Message": "Data generated"}


@app.get("/pull_data/{country}")
def foo_pull_data(country: str):
    engine = pg.connect(f"dbname={DATABASE_NAME} user={DATABASE_USER_NAME} host={DATABASE_HOST} port={DATABASE_PORT} password={DATABASE_PASSWORD}")
    df = pd.read_sql(f'select * from {country}', con=engine)
    return {"Message": "Data pulled", "Data": df.to_json()}