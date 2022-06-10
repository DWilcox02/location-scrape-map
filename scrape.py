import requests
from bs4 import BeautifulSoup
from location import Location

def scrapeLocations():
    r = requests.get("https://www.tourisme-colmar.com/en/visit/presentation/architectural-heritage")
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    cards = soup.find_all("li", {"class": "jsit-item"})

    home = Location("Home", "1 Rue de l'Ancienne Mairie, 68000 Colmar, France", "Home")

    locations = [home]

    for card in cards:
        locationType = card.find("div", {"class": "uk-position-top-left"}).text.strip()
        link = card.find("a", {"class": "uk-position-cover"})["href"]
        name = card.find("a", {"class": "uk-position-cover"})["title"]
        cardRequest = requests.get("https://www.tourisme-colmar.com" + link)
        cardContent = cardRequest.content
        cardSoup = BeautifulSoup(cardContent, "html.parser")
        address = cardSoup.find("div", {"class": "uk-width-3-4"}).find("div", {"itemprop": "address"}).text.strip()
        location = Location(name, address, locationType)
        locations.append(location)

    return locations

