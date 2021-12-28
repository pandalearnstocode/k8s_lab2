import redis

from app.worker import celery
from app.config import REDIS_STORE_CONN_URI

redis_store = redis.Redis.from_url(REDIS_STORE_CONN_URI)


@celery.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage