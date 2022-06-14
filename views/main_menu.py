import os

class MainMenu:
    @staticmethod
    def render():
        os.system('clear')
        print('----------')
        print('1. Start vaccination proccess')
        print('2. Patients menu')
        print('3. Professionals menu\n')
        print('0. Exit')

        return input('\n-> ')