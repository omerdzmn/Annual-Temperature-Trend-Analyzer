🌍 Climate Change Analysis – Istanbul / Kadıköy
📌 Project Summary

This project analyzes long-term temperature changes in the Kadıköy district of Istanbul to observe local climate change effects.
Daily temperature data is collected from an external meteorological archive, cleaned, aggregated, and visualized using anomaly analysis.

📍 Study Area

Location: Istanbul / Kadıköy

Coordinates: 40.9917° N, 29.0275° E

Time Period: 1950 – 2024

The data represents measurements from the station closest to Kadıköy’s geographic center.

📊 Data Source

Source: Open-Meteo Archive API

Data Type: Daily temperature measurements

Variables: Mean, minimum, and maximum temperature (°C)

The data is fetched dynamically via HTTP requests.

🧹 Data Preparation

The raw daily data is considered messy and processed using the following steps:

Date conversion and time extraction

Removal of missing values

Calculation of average temperature if necessary

Aggregation from daily to monthly and yearly averages

Cleaned data is stored in:
data/processed/climate_cleaned.csv

📈 Analysis Method

The analysis focuses on temperature anomalies.

Annual Average Temperature: Average of daily temperatures within a year

Long-Term Average: Mean temperature across all years

Anomaly: Difference between yearly temperature and long-term average

This method highlights warmer and cooler years clearly.

🎨 Visualization

The visualization includes:

A line showing yearly average temperature

Colored points representing anomalies

A reference line for long-term average

Color meaning:

🔴 Red → Warmer-than-average years

🔵 Blue → Cooler-than-average years

🔍 Key Findings

Long-term average temperature in Kadıköy is approximately 14.5 °C

Warmer years become more frequent after 2000

Results indicate a clear local warming trend

📂 Project Structure

havadurumu/
├─ data/
│  ├─ raw/
│  └─ processed/
├─ src/
│  ├─ scraping/
│  ├─ cleaning/
│  └─ analysis/
├─ main.py
└─ README.md



▶️ How to Run
pip install pandas matplotlib requests
python main.py



🎓 Academic Purpose

This project demonstrates:

External data collection

Messy data cleaning

Statistical aggregation

Anomaly-based climate analysis

Scientific visualization