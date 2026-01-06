# 🌍 Climate Change Analysis – Istanbul / Kadıköy

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Subject](https://img.shields.io/badge/Subject-Climate%20Analysis-green)

## 📌 Project Summary
This project analyzes long-term temperature changes in the **Kadıköy** district of Istanbul to observe local climate change effects.
Daily temperature data is collected from an external meteorological archive, cleaned, aggregated, and visualized using anomaly analysis.

---

## 📍 Study Area
* **Location:** Istanbul / Kadıköy
* **Coordinates:** 40.9917° N, 29.0275° E
* **Time Period:** 1950 – 2024

> *The data represents measurements from the station closest to Kadıköy’s geographic center.*

---

## 📊 Data Source
* **Source:** Open-Meteo Archive API
* **Data Type:** Daily temperature measurements
* **Variables:** Mean, Minimum, and Maximum temperature (°C)
* **Method:** The data is fetched dynamically via HTTP requests.

---

## 📂 Project Structure

```text
havadurumu/
├── data/
│   ├── raw/           # Raw downloaded data
│   └── processed/     # Cleaned CSV files
├── src/
│   ├── scraping/      # Data collection scripts
│   ├── cleaning/      # Data preprocessing scripts
│   └── analysis/      # Statistical analysis scripts
├── main.py            # Main execution file
└── README.md          # Project documentation

## 🧹 Data Preparation
The raw daily data is considered messy and processed using the following steps:

1.  Date conversion and time extraction.
2.  Removal of missing values (NaN).
3.  Calculation of average temperature if necessary.
4.  Aggregation from daily to monthly and yearly averages.

💾 **Output:** Cleaned data is stored in `data/processed/climate_cleaned.csv`.

---

## 📈 Analysis Method
The analysis focuses on **temperature anomalies**:

* **Annual Average Temperature:** Average of daily temperatures within a year.
* **Long-Term Average:** Mean temperature across all years (1950-2024).
* **Anomaly:** (Yearly Temperature) - (Long-Term Average).

🔴 **Red:** Warmer-than-average years.  
🔵 **Blue:** Cooler-than-average years.

---

## 🔍 Key Findings
* Long-term average temperature in Kadıköy is approximately **14.5 °C**.
* **Warmer years** become more frequent after the year **2000**.
* Results indicate a clear **local warming trend**.

---

## 🎨 Visualization
The visualization includes:
* A line showing yearly average temperature.
* Colored points representing anomalies.
* A reference line for long-term average.

---

## ▶️ How to Run

To set up the environment and run the analysis, use the following commands:

```bash
# Install required libraries
pip install pandas matplotlib requests

# Run the main script
python main.py
