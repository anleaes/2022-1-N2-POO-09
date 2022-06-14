from datetime import date
from datetime import datetime
import sys
sys.path.append('..')
from store.store import Store

class Ampoule:
    def __init__(self, name, description, laboratory, store: Store):
        self.__id        = store.ampoules.getNewId()
        self.name        = name
        self.description = description
        self.laboratory  = laboratory

    def getId(self):
        return self.__id

    def setExpiresAt(self, month, year):
        self.__expiresAt = datetime(year, month)

    def getExpiresAt(self, format = '%m/%Y'):
        return self.__expiresAt.strftime(format)
