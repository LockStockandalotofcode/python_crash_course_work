from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/san_francisco_2025.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# print(header_row) 

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates, low and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')#.date()
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# print(highs)

# plot the high and low temperatures.
fig, ax = plt.subplots(figsize=(15, 9))
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021\nSan Francisco", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()