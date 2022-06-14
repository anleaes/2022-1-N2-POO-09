from datetime import date
from datetime import datetime
import sys
sys.path.append('..')
from store.store import Store

class Patient:
    def __init__(self, name, cpfCnpj, email, store: Store) -> None:
        self.name        = name
        self.cpfCnpj     = cpfCnpj
        self.email       = email
        self.__birthDate = None
        self.id          = self.getId(store)

    @staticmethod
    def getId(store: Store)->int:
        return store.patients.getNewId()

    def setBirthDate(self, year, month, day):
        self.__birthDate = datetime(year, month, day)

    def getBirthDate(self, format = '%d/%m/%Y'):
        return self.__birthDate.strftime(format)
