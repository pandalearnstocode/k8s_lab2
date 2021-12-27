import os

from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache
from sqlalchemy.orm import Session

LOCAL_REDIS_URL = "redis://redis-service:6379"

app = FastAPI(title="FastAPI Redis Cache Example")

@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )

@app.get("/")
def read_main():
    return {"ping": "pong", "root_path": "applicationlayer"}


subapi = FastAPI()


@subapi.get("/app")
def read_sub():
    return {"ping": "pong", "root_path": "applicationlayer/app"}

@subapi.get("/data_no_cache")
def get_data():
    return {"success": True, "message": "this data is not cacheable, for... you know, reasons"}

# Will be cached for one year
@subapi.get("/immutable_data")
@cache()
async def get_immutable_data():
    return {"success": True, "message": "this data can be cached indefinitely"}

@subapi.get("/dynamic_data")
@cache(expire=30)
def get_dynamic_data(request: Request, response: Response):
    return {"success": True, "message": "this data should only be cached temporarily"}

app.mount("/applicationlayer", subapi)
