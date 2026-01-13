from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('./weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

dates, rainfalls = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d').date()
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"Missing Data for {date}")
    else:
        dates.append(date)
        rainfalls.append(rainfall)

# plot the rainfall.
fig, ax = plt.subplots(figsize=(15, 9))
ax.bar(dates, rainfalls) # does not work for float rainfall data type and date 
# ax.bar(rainfalls)

# Format plot.
ax.set_title("Daily rainfall, 2025\nSitka, Alaska", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()