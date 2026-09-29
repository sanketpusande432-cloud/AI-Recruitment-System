import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)

def save_screening_result(key, result):

    redis_client.setex(
        key,
        3600,
        json.dumps(result)
    )


def get_screening_result(key):

    result = redis_client.get(key)

    if result:
        return json.loads(result)

    return None