import folium
import pandas as pd

df = pd.read_csv("Locations.csv")

map=folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()])