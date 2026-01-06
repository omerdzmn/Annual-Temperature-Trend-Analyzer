import os
import pandas as pd


def clean_data():
    """
    Clean daily temperature data and
    aggregate it into monthly averages.
    """

    df = pd.read_csv("data/raw/climate_raw.csv")

    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    df = df.dropna(subset=["time"])

    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month

    if "tavg" not in df.columns or df["tavg"].isna().all():
        df["tavg"] = (df["tmin"] + df["tmax"]) / 2

    monthly = df.groupby(["year", "month"], as_index=False)["tavg"].mean()

    os.makedirs("data/processed", exist_ok=True)
    monthly.to_csv("data/processed/climate_cleaned.csv", index=False)

    print("✅ Cleaned monthly data saved")
