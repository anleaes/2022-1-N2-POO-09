import os

class Index:
    def __init__(self, patients):
        self.patients = patients

        os.system('clear')

        print('👤 List of patients: \n')

        for patient in patients:
            print('ID: ' + patient.id + 'Name: ' + patient.name + 'CPF/CNPJ: ' + patient.cpfCnpj + 'Email: ' + patient.email)
