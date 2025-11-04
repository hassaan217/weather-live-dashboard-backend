# app/services/weather_service.py
import httpx
from typing import Dict, Any
from app.core.config import settings

class WeatherService:
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = settings.OPENWEATHER_BASE_URL
    
    async def get_current_weather(self, city: str) -> Dict[str, Any]:
        """Get current weather data for a city."""
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_daily_forecast(self, city: str) -> Dict[str, Any]:
        """Get 7-day weather forecast for a city."""
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "cnt": 40  # 7 days * 8 forecasts per day (every 3 hours)
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_hourly_forecast(self, city: str) -> Dict[str, Any]:
        """Get 24-hour weather forecast for a city."""
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "cnt": 8  # 24 hours / 3 = 8 forecasts
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_geo_location(self, city: str) -> Dict[str, Any]:
        """Get geographical data for a city."""
        # We can use the current weather endpoint to get geo data
        weather_data = await self.get_current_weather(city)
        return {
            "name": weather_data["name"],
            "coord": weather_data["coord"],
            "sys": weather_data["sys"]
        }

weather_service = WeatherService()