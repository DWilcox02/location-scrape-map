import webbrowser
import folium
import pandas as pd

df = pd.read_csv("Locations.csv")

map=folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=16, control_scale=True)

def setColour(locationType):
    colour = ""
    if locationType == "home":
        colour = "red"
    elif locationType == "remarkable house":
        colour = "blue"
    elif locationType == "remarkable buildings":
        colour = "blue"
    elif locationType == "fountain":
        colour = "purple"
    elif locationType == "museum":
        colour = "pink"
    elif locationType == "monument":
        colour = "orange"
    elif locationType == "park or square":
        colour = "green"
    elif locationType == "religious building":
        colour = "white"
    elif locationType == "district":
        colour = "lightblue"
    else:
        colour = "black"
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