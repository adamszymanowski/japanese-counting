FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY populate_redis.py .

CMD ["python", "populate_redis.py"]
