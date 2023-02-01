import webbrowser
import folium
import pandas as pd

df = pd.read_csv("Locations.csv")

map=folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=16, control_scale=True)

colours = {
    "home": "red",
    "remarkable house": "blue",
    "remarkable buildings": "blue",
    "fountain": "purple",
    "museum": "pink",
    "monument": "orange",
    "park or square": "green",
    "religious building": "white",
    "district" : "lightblue"
}

def setColour(locationType):
    colour = colours[locationType]
    if colour == None:
        return "black"
    return colour

for index, locationInfo in df.iterrows():
    colour = ""
    locationType = locationInfo["Type"]
    try:
        locationType = locationType.lower()
        colour = setColour(locationType)
    except:
        colour = "black"
    icon = folium.Icon(color=colour, icon_color="white")
    try:
        folium.Marker([locationInfo["Latitude"], locationInfo["Longitude"]], popup=locationInfo["Name"], icon=icon).add_to(map)
    except:
        pass

map.save("map.html")
webbrowser.open("map.html")