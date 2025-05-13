# COVID-19 Global Tracker (Without pandas)
# ========================================
# This version uses the built-in csv module and matplotlib only

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# ---- Step 1: Load Data ----
data = {
    "Kenya": [],
    "United States": [],
    "India": []
}

try:
    with open("owid-covid-data.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row["location"]
            if country in data and row["date"]:
                try:
                    date = datetime.strptime(row["date"], "%Y-%m-%d")
                    total_cases = float(row["total_cases"]) if row["total_cases"] else 0
                    total_deaths = float(row["total_deaths"]) if row["total_deaths"] else 0
                    total_vaccinations = float(row["total_vaccinations"]) if row["total_vaccinations"] else 0
                    new_cases = float(row["new_cases"]) if row["new_cases"] else 0

                    data[country].append({
                        "date": date,
                        "cases": total_cases,
                        "deaths": total_deaths,
                        "vaccinations": total_vaccinations,
                        "new_cases": new_cases
                    })
                except ValueError:
                    continue
except FileNotFoundError:
    print("❌ File not found. Please make sure 'owid-covid-data.csv' is in your working folder.")
    exit()

# ---- Step 2: Sort Data by Date ----
for country in data:
    data[country].sort(key=lambda x: x["date"])

# ---- Step 3: Plot Total Cases ----
plt.figure(figsize=(10, 6))
for country, records in data.items():
    dates = [record["date"] for record in records]
    cases = [record["cases"] for record in records]
    plt.plot(dates, cases, label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ---- Step 4: Plot Total Deaths ----
plt.figure(figsize=(10, 6))
for country, records in data.items():
    dates = [record["date"] for record in records]
    deaths = [record["deaths"] for record in records]
    plt.plot(dates, deaths, label=country)

plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ---- Step 5: Plot Total Vaccinations ----
plt.figure(figsize=(10, 6))
for country, records in data.items():
    dates = [record["date"] for record in records]
    vaccinations = [record["vaccinations"] for record in records]
    plt.plot(dates, vaccinations, label=country)

plt.title("Cumulative COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ---- Step 6: Plot New Daily Cases ----
plt.figure(figsize=(10, 6))
for country, records in data.items():
    dates = [record["date"] for record in records]
    new_cases = [record["new_cases"] for record in records]
    plt.plot(dates, new_cases, label=country)

plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ---- Step 7: Basic Summary ----
print("\n📈 Summary of Latest Data:")
for country, records in data.items():
    if records:
        latest = records[-1]
        print(f"{country} (as of {latest['date'].strftime('%Y-%m-%d')}):")
        print(f"  Total Cases: {int(latest['cases']):,}")
        print(f"  Total Deaths: {int(latest['deaths']):,}")
        print(f"  Total Vaccinations: {int(latest['vaccinations']):,}\n")
