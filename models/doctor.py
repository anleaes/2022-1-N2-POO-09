from professional import Professional

import sys
sys.path.append('..')
from store.store import Store

class Doctor(Professional):
    def __init__(self, name, store: Store):
        Professional.__init__(name)
        self.__id = store.doctors.getNewId()

    def getId(self):
        return self.__id
