import redis
import json


redis_client = redis.Redis(
    host="localhost",
    port=6379,
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