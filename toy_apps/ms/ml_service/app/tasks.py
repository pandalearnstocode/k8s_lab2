import redis

from app.worker import celery
from app.config import CACHE_REDIS_URL

redis_store = redis.Redis.from_url(CACHE_REDIS_URL)


@celery.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage