import sys
sys.path.append('..')

from views.main_menu import MainMenu
from controllers.patient_controller import PatientController
from store.store import Store

class MainMenuController:

    @staticmethod
    def Index(store: Store)->bool:
        EXIT              = 0
        LIST_PATIENTS     = 1
        CREATE_PATIENTS   = 2

        response = MainMenu.render()

        if response == EXIT:
            return False

        if response == LIST_PATIENTS:
            PatientController.listPatients(store)

        if response == CREATE_PATIENTS:
            PatientController.createPatient(store)

        return True
