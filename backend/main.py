from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Satellite Tracker API")

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Satellite Tracker API Running"}
    