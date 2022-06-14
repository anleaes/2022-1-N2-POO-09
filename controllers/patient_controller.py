import sys
sys.path.append('..')
from store.store import Store
from views.patients.index import Index

class PatientController:
    def __init__(self, store: Store):
        self.store = store

    def listPatients(self):
        patients = self.store.patients.all()

        Index(patients)

