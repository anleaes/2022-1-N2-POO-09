from controllers.main_menu_controller import MainMenuController
from store.store import Store

store = Store()

def run(shouldKeepRunning):
    if not shouldKeepRunning:
        return

    shouldKeepRunning = MainMenuController.Index(store)

run(True)
