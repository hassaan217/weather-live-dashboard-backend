# Weather Insight Dashboard Backend

FastAPI backend for the Weather Insight Dashboard application. Provides weather data from OpenWeatherMap API and stores search history in MongoDB.

## Features

- RESTful API for weather data
- Integration with OpenWeatherMap API
- MongoDB for storing search history
- CORS support for frontend integration
- Environment configuration

## Tech Stack

- **Framework**: FastAPI
- **Database**: MongoDB Atlas
- **Weather Data**: OpenWeatherMap API
- **HTTP Client**: httpx
- **Configuration**: python-dotenv

## Setup Instructions

### Prerequisites

- Python 3.8+
- MongoDB Atlas account
- OpenWeatherMap API key

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/weather-insight-dashboard.git
   cd weather-insight-dashboard/backend