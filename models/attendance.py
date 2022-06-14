from datetime import date

import sys
sys.path.append('..')
from store.store import Store

class Attendance:
    def __init__(self, professional, patient, room, store: Store):
        self.__id           = store.attendances.getNewId()
        self.professional = professional
        self.patient      = patient
        self.room         = room
        self.__attendedAt = None

    def getId(self):
        return self.__id

    def markAsAttended(self):
        self.__attendedAt = date.today()

    def getAttendedAt(self, format = '%d/%m/%Y'):
        return self.__attendedAt.strftime(format)
