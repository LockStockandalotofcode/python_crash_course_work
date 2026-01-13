from pathlib import Path
import csv 

import matplotlib.pyplot as plt

path = Path('weather_data/nashville_data.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)
# ['STATION', 'NAME', 'DATE', 'DAPR', 'MDPR', 'PRCP', 'SNOW', 'SNWD']