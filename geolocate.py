import pandas as pd
from geopandas import *
from geopy import *
import scrape

def geoLocate():
    locations = scrape.scrapeLocations()

    locator = Nominatim(user_agent="myGeocoder")

    for location in locations:
        geocodeUnit = locator.geocode(location.getAddress())
        location.applyGeolocation(geocodeUnit)
        
    df = pd.DataFrame.from_records([l.to_dict() for l in locations])
    df.to_csv("Locations.csv")