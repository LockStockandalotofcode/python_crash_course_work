from pathlib import Path
import csv
import json

import plotly.express as px

# Read data as a string and convert to a python object.
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

lats, lons, brightness = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    brightnes = float(row[2])

    lats.append(lat)
    lons.append(lon)
    brightness.append(brightnes)




# contents = path.read_text()
# all_eq_data = json.loads(contents)

# # # Create a more readable version of the data file.
# # path = Path('eq_data/readable_eq_data.geojson')
# # readable_contents = json.dumps(all_eq_data, indent=4)
# # path.write_text(readable_contents)

# # Examine all the earthquakes in the dataset.
# all_eq_dicts = all_eq_data['features']
# # print(len(all_eq_dicts))

# mags, lons, lats, eq_titles = [], [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     eq_title = eq_dict['properties']['title']

#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)
#     eq_titles.append(eq_title)

# # print(mags[:10])
# # print(lons[:5])
# # print(lats[:5])

title = 'World Fires 1 day'
fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, title=title,
        color=brightness,
        color_continuous_scale='bluered', # bluered, icefire, tealrose, 
        labels={'color':"Brightness"},
        projection='natural earth',
    )
fig.show()
