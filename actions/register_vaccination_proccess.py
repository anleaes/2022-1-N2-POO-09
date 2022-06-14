import os
from re import I
import sys
sys.path.append('..')
from store.store import Store
from models.patient import Patient
from models.attendance import Attendance

class RegisterAttendance:
    def __init__(self, store: Store):
        self.store = store

        self.professionalTypes = {
            1: 'DOCTOR',
            2: 'NURSE',
        }

    def run(self)->Attendance:
        self.selectedPatient      = self.getPatient()
        self.selectedProfessional = self.getProfessional()
        self.selectedRoom         = self.getRoom()

        return Attendance(self.selectedPatient, self.selectedProfessional, self.selectedRoom)

    def getPatient(self)->Patient:
        print('Please, input the patient ID.')

        patientId = input('\n-> ')

        return self.store.patients.find(patientId)

    def getProfessional(self, type):
        os.system('clear')

        selectedType = None

        while selectedType != self.professionalTypes['DOCTOR'] or selectedType != self.professionalTypes['NURSE']:
            print(self.patient.name + 'selected ✅ \n')
            print('What is the professional type responsible for the attendance?')
            print('1. Nurse')
            print('2. Doctor')

            self.selectedType = input('\n-> ')

        os.system('clear')

        print(self.patient.name + ' selected ✅')
        print(self.professionalTypes[self.selectedType] + ' selected ✅')

        input('\nPlease, input the ' + self.professionalTypes[self.selectedType])

        if selectedType == self.professionalTypes['DOCTOR']:
            return self.store.doctors.find()

        if selectedType == self.professionalTypes['NURSE']:
            return self.store.nurses.find()

    def getRoom(self):
        os.system('clear')

        print(self.patient.name + ' selected ✅')
        print(self.professionalTypes[self.selectedPatient] + ' ' + self.selectedProfessional.name + ' selected ✅')
        print('\nType the room code: ')

        return input('-> ')