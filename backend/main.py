from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router
from backend.services.scheduler import start_scheduler


app = FastAPI(
    title="Real-Time Satellite Tracker API"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router)


@app.on_event("startup")
def startup():
    start_scheduler()


@app.get("/")
def home():
    return {"message": "Satellite Tracker API running"}