from datetime import date
from datetime import datetime

import sys
sys.path.append('..')
from store.store import Store

class Campaign:
    def __init__(self, illnessName, minAge, maxAge, store: Store):
        self.__id        = store.campaigns.getNewId()
        self.illnessName = illnessName
        self.minAge      = minAge
        self.maxAge      = maxAge
        self.__startedAt = None
        self.__endedAt   = None

    def getId(self):
        return self.__id

    def getStartedAt(self, format = '%d/%m/%Y'):
        return self.__startedAt.strftime(format)

    def setStartedAt(self, year, month, day):
        self.__startedAt = datetime(year, month, day)

    def getEndedAt(self, format = '%d/%m/%Y'):
        return self.__endedAt.strftime(format)

    def setEndedAt(self, year, month, day):
        self.__endedAt = datetime(year, month, day)
