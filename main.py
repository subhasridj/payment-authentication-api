from fastapi import FastAPI
from api.routes import auth

app = FastAPI(title="Secure Login & Register API")

app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Welcome! Go to /docs to test Register & Login APIs"}
