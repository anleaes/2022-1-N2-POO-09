import sys
sys.path.append('..')
from store.store import Store
from views.patients.index import Index
from views.patients.create import Create
from models.patient import Patient

class PatientController:
    def __init__(self, store: Store):
        self.store = store

    def listPatients(self):
        patients = self.store.patients.all()

        Index(patients)

    def createPatient(self):
        response = Create.render()

        patient = Patient(response.name, response.cpfCnpj, response.email)

        self.store.patients.add(patient)

        Create.success()
