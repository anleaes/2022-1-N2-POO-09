import sys
sys.path.append('..')
from store.store import Store

class Laboratory:
    def __init__(self, name, localization, store: Store):
        self.__id        = store.laboratories.getNewId()
        self.localization = localization
        self.name         = name

    def getId(self):
        return self.__id