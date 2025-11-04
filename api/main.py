# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import weather
from app.db.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Weather Insight Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
    "https://live-weather-dash.vercel.app",
    "https://weather-live-dashboard.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add event handlers for MongoDB connection
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

# Include routes
app.include_router(weather.router, prefix="/api", tags=["weather"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Weather Insight Dashboard API"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)