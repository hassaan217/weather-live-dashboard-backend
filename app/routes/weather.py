# app/routers/weather.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any
from bson import ObjectId
from app.services.weather_service import weather_service
from app.db.database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/weather/current")
async def get_current_weather(city: str, db=Depends(get_db)):
    """Get current weather for a city."""
    try:
        weather_data = await weather_service.get_current_weather(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/weather/forecast/daily")
async def get_daily_forecast(city: str, db=Depends(get_db)):
    """Get 7-day weather forecast for a city."""
    try:
        forecast_data = await weather_service.get_daily_forecast(city)
        return forecast_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/weather/forecast/hourly")
async def get_hourly_forecast(city: str, db=Depends(get_db)):
    """Get 24-hour weather forecast for a city."""
    try:
        hourly_data = await weather_service.get_hourly_forecast(city)
        return hourly_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/geo/location")
async def get_geo_location(city: str, db=Depends(get_db)):
    """Get geographical data for a city."""
    try:
        geo_data = await weather_service.get_geo_location(city)
        return geo_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/search/save")
async def save_search(city: str, db=Depends(get_db)):
    """Save a city search to the database."""
    try:
        search_data = {
            "city": city,
            "timestamp": datetime.utcnow()
        }
        
        result = db.searches.insert_one(search_data)
        
        saved_search = db.searches.find_one({"_id": result.inserted_id})
        saved_search["_id"] = str(saved_search["_id"])
        
        return saved_search
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving search: {str(e)}")

@router.get("/search/recent")
async def get_recent_searches(db=Depends(get_db)):
    """Get recent search history."""
    try:
        searches = list(db.searches.find().sort("timestamp", -1).limit(10))
        
        for search in searches:
            search["_id"] = str(search["_id"])
        
        return searches
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recent searches: {str(e)}")