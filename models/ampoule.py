from datetime import date
from datetime import datetime

class Ampoule:
    def __init__(self, name, description, laboratory):
        self.name = name
        self.description = description
        self.laboratory = laboratory

    def setExpiresAt(self, month, year):
        self.__expiresAt = datetime(year, month)

    def getExpiresAt(self, format = '%m/%Y'):
        return self.__expiresAt.strftime(format)
