

from mimetypes import init


class Location():


    def __init__(self, address, type) -> None:
        self.address = address
        self.type = type

    def getAddress(self):
        return self.address
    
    def getType(self):
        return self.type