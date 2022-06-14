from datetime import date
from datetime import datetime

import sys
sys.path.append('..')
from store.store import Store

class Patient:
    def __init__(self, name, cpfCnpj, email, store: Store) -> None:
        self.__id        = store.patients.getNewId()
        self.name        = name
        self.cpfCnpj     = cpfCnpj
        self.email       = email
        self.__birthDate = None

    def getId(self):
        return self.__id

    def setBirthDate(self, year, month, day):
        self.__birthDate = datetime(year, month, day)

    def getBirthDate(self, format = '%d/%m/%Y'):
        return self.__birthDate.strftime(format)
