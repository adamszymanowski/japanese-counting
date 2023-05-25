import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)

numbers = {
    "1": "一",
    "2": "二",
    "3": "三",
    # Add the rest of your numbers here...
}

for key, value in numbers.items():
    redis_client.set(key, value)
