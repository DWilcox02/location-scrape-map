

from mimetypes import init


class Location():


    def __init__(self, name, address, type="") -> None:
        self.name = name
        self.address = address
        self.type = type

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address
    
    def getType(self):
        return self.type

    def applyGeolocation(self, geolocation):
        self.geolocation = geolocation
        try:
            self.latitude = self.geolocation.latitude
            self.longitude = self.geolocation.longitude
        except:
            self.latitude = None
            self.longitude = None
            print(self.name)
    
    def getGeolocation(self):
        return self.geolocation

    def to_dict(self):
        return {
            "Name": self.name,
            "Type": self.type,
            "Address": self.address,
            "Latitude": self.latitude,
            "Longitude": self.longitude
        }