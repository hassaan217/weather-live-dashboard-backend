# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY")
    OPENWEATHER_BASE_URL: str = "https://api.openweathermap.org/data/2.5"
    
    MONGODB_URI: str = os.getenv("MONGODB_URI")
    
    APP_NAME: str = os.getenv("APP_NAME", "Weather Insight Dashboard")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()