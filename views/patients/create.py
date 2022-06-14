import os

class Create:
    @staticmethod
    def render()->list:
        data = {}

        os.system('clear')

        print('👤 Create new patient!')

        print('\nInsert their name:')
        data['name'] = input('-> ')

        print('\nInsert their CPF/CNPJ:')
        data['cpfCnpj'] = input('-> ')

        print('\nInsert their email:')
        data['email'] = input('-> ')

        return data

    def success():
        os.system('clear')

        print('Patient successfully created ✅')