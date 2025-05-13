# CovidTracker

# 🦠 COVID-19 Global Data Tracker (No Pandas Version)

A simplified Python project that tracks and visualizes global COVID-19 data for Kenya, the United States, and India using only built-in modules and `matplotlib`. It processes real-world data from Our World in Data to generate insights on total cases, deaths, daily new cases, and vaccinations — all without using `pandas`.

---

## 🎯 Project Objectives

- Load and process a CSV COVID-19 dataset without using pandas
- Analyze and compare COVID-19 trends across selected countries
- Visualize time-series data on cases, deaths, vaccinations, and daily new cases
- Generate a simple report with charts and printed summaries

---

## 🧰 Tools & Libraries Used

- Python 3.x
- `csv` (built-in)
- `datetime` (built-in)
- [`matplotlib`](https://matplotlib.org/) – for plotting charts

---

## ▶️ How to Run the Project

1. Download the dataset: [Our World in Data COVID-19 CSV](https://covid.ourworldindata.org/data/owid-covid-data.csv)
2. Save it as `owid-covid-data.csv` in the same folder as your Python script.
3. Make sure you have `matplotlib` installed:

   ```bash
   pip install matplotlib
   ```

4. Run the script:

   ```bash
   python CovidTracker.py
   ```

This will generate line plots for total cases, deaths, vaccinations, and daily new cases for Kenya, the USA, and India.

---

## 📈 Insights & Reflections

- The USA shows the highest numbers in both total cases and vaccinations.
- India experienced multiple spikes in daily new cases over time.
- Kenya’s vaccination rollout is slower but steadily increasing.
- Visualizing data without pandas is possible but less flexible and scalable.

---

## 📦 Optional Enhancements

- Add more countries or metrics (e.g., % vaccinated population)
- Export charts to images
- Create an interactive dashboard (using Tkinter or Plotly)

---

© 2025 – Built with Python & curiosity 💡
