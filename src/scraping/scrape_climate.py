import os
import requests
import pandas as pd

LAT = 40.9917   # Kadıköy latitude
LON = 29.0275   # Kadıköy longitude


def scrape_climate():
    """
    Fetch daily temperature data for Istanbul / Kadıköy
    using the Open-Meteo Archive API.
    """

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "start_date": "1950-01-01",
        "end_date": "2024-12-31",
        "daily": "temperature_2m_mean,temperature_2m_min,temperature_2m_max",
        "timezone": "UTC"
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()

    daily = data["daily"]

    df = pd.DataFrame({
        "time": daily["time"],
        "tavg": daily["temperature_2m_mean"],
        "tmin": daily["temperature_2m_min"],
        "tmax": daily["temperature_2m_max"]
    })

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/climate_raw.csv", index=False)

    print("✅ Raw climate data saved (Kadıköy)")
