from fastapi import FastAPI
from app.utils import generate_fake_dataframe, pandas_to_sql
import os
import pandas as pd
import psycopg2 as pg

from app.config import DATALAKE_DATABASE_URL, DATALAKE_DATABASE_NAME, DATALAKE_DATABASE_HOST, DATALAKE_DATABASE_USER_NAME, DATALAKE_DATABASE_PASSWORD, DATALAKE_DATABASE_PORT

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
    pandas_to_sql(dburi=DATALAKE_DATABASE_URL, df = df, table_name=country)
    return {"Message": "Data generated"}


@app.get("/pull_data/{country}")
def foo_pull_data(country: str):
    engine = pg.connect(f"dbname={DATALAKE_DATABASE_NAME} user={DATALAKE_DATABASE_USER_NAME} host={DATALAKE_DATABASE_HOST} port={DATALAKE_DATABASE_PORT} password={DATALAKE_DATABASE_PASSWORD}")
    df = pd.read_sql(f'select * from {country}', con=engine)
    return {"Message": "Data pulled", "Data": df.to_json()}