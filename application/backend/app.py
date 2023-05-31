from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import redis
from os import getenv

# Fast API setup
app = FastAPI()

env_var = "APPLICATION_ENVIRONMENT"
application_environment = getenv(env_var, "Unknown")
development = (application_environment == "DEVELOPMENT")
if development:
    origins = [
        "http://localhost:8000",  # Svelte app port
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# prepare data
data = {}
data[env_var] = application_environment

# redis
redis_client = redis.Redis(host='redis', port=6379, db=0)
data["1"] = redis_client.get("1")

@app.get("/")
def read_root():
    return data


@app.get("/development_message")
def development_message():
    if development:
        return {"message": "This is a development environment!"}
    else:
        raise HTTPException(status_code=404, detail="Not found")
