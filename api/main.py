from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import weather
from app.db.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Weather Insight Dashboard API")

# ✅ CORS Setup
origins = [
    "http://localhost:5173",  # for local dev
    "https://weather-live-dashboard.vercel.app",  # your frontend deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(weather.router, prefix="/api", tags=["weather"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Weather Insight Dashboard API"}
