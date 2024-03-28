import geopandas as gpd
import matplotlib.pyplot as plt


detroit = gpd.read_file('City_of_Detroit_Boundary.shp')

fig, ax = plt.subplots(figsize=(10, 10))
detroit.plot(ax=ax, color='skyblue', edgecolor='black')
plt.title('Map of Detroit')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()