# 🌍 Climate Change Analysis — Istanbul / Kadıköy

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Subject](https://img.shields.io/badge/Subject-Climate%20Analysis-yellow)

---

## 📌 Project Summary
This project analyzes long-term temperature changes in **Kadıköy (Istanbul)** to observe local climate trends. Daily temperature data is fetched from an external API, cleaned, aggregated, and visualized using **temperature anomaly analysis**.

---

## 📍 Study Area
- **Location:** Istanbul / Kadıköy  
- **Coordinates:** 40.9917° N, 29.0275° E  
- **Time Period:** 1950 – 2024  

> The dataset represents measurements from the data source closest to Kadıköy’s geographic center.

---

## 🗂️ Data Source
- **Source:** Open-Meteo Archive API  
- **Data Type:** Daily temperature measurements  
- **Variables:** Mean / Minimum / Maximum temperature (°C)  
- **Method:** Data is fetched dynamically via HTTP requests

---

## 🧹 Data Preparation
The raw daily dataset is processed with these steps:
- Date parsing (time conversion)
- Missing value handling (NaN cleanup)
- Average temperature calculation (when needed)
- Aggregation from **daily → monthly → yearly**

✅ Output file:
- `data/processed/climate_cleaned.csv`

---

## 📈 Analysis Method (Anomalies)
We compute:
- **Annual Average Temperature:** mean of daily temperatures in each year  
- **Long-Term Average:** mean temperature across all years (1950–2024)  
- **Anomaly:**  
  **Anomaly = (Yearly Average) − (Long-Term Average)**

This highlights **warmer** and **cooler** years clearly.

---

## 🎨 Visualization
The plot includes:
- A line for **yearly average temperature**
- Colored points for **anomalies**
- A dashed reference line for the **long-term average**

**Color meaning:**
- 🔴 Red → Warmer-than-average years  
- 🔵 Blue → Cooler-than-average years  

---

## 🔍 Key Findings
- Long-term average temperature in Kadıköy is approximately **14.5 °C**
- Warmer years become more frequent after **2000**
- Results indicate a clear **local warming trend**

---

## 📂 Project Structure
```text
havadurumu/
├─ data/
│  ├─ raw/                # Raw downloaded data
│  └─ processed/          # Cleaned CSV output
├─ src/
│  ├─ scraping/           # Data collection
│  ├─ cleaning/           # Data preprocessing
│  └─ analysis/           # Anomaly analysis + plotting
├─ outputs/               # Generated figures (if saved)
├─ main.py                # Main entry point
├─ requirements.txt       # Dependencies
└─ README.md              # Documentation
