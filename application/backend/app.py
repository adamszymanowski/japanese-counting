from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from os import getenv

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

@app.get("/")
def read_root():
    return {env_var: application_environment}


@app.get("/development_message")
def development_message():
    if development:
        return {"message": "This is a development environment!"}
    else:
        raise HTTPException(status_code=404, detail="Not found")
