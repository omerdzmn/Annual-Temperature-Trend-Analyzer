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
