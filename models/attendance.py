from datetime import date
from re import I

class Attendance:
    def __init__(self, professional, patient, attendedAt):
        self.professional = professional
        self.patient      = patient
        self.__attendedAt   = attendedAt

    def markAsAttended(self):
        self.__attendedAt = date.today()

    def getAttendedAt(self, format = '%d/%m/%Y'):
        return self.__attendedAt.strftime(format)
