import sys
sys.path.append('..')
from store.store import Store
from views.patients.index import Index
from views.patients.create import Create
from models.patient import Patient

class PatientController:
    @staticmethod
    def listPatients(store: Store):
        patients = store.patients.all()

        Index(patients)

    @staticmethod
    def createPatient(store: Store):
        response = Create.render()

        patient = Patient(response.name, response.cpfCnpj, response.email)

        store.patients.add(patient)

        Create.success()
