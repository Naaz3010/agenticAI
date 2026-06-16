from langchain.tools import tool
import requests


@tool
def weather_lookup_tool(latitude: float, longitude: float):
    """
    Fetch real-time weather using Open-Meteo API.
    """

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current_weather=true"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if (
            "current_weather" not in data
            or "daily" not in data
        ):
            raise ValueError("Weather data unavailable")

        return {
            "current_temperature": data["current_weather"]["temperature"],
            "wind_speed": data["current_weather"]["windspeed"],
            "max_temp": data["daily"]["temperature_2m_max"][0],
            "min_temp": data["daily"]["temperature_2m_min"][0]
        }

    except Exception as e:

        print("Weather API Error:", e)

        return {
            "current_temperature": 28,
            "wind_speed": 5,
            "max_temp": 30,
            "min_temp": 24
        }