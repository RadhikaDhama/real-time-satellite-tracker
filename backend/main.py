from fastapi import FastAPI
from backend.api.routes import router
from backend.services.scheduler import start_scheduler
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Real-Time Satellite Tracker API"
)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():

    start_scheduler()


@app.get("/")
def home():

    return {"message":"Satellite Tracker API running"}