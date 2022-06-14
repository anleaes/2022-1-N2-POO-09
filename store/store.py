from states.nurses import Nurses
from states.doctors import Doctors
from states.patients import Patients
from states.ampoules import Ampoules
from states.campaigns import Campaigns
from states.attendances import Attendances
from states.laboratories import Laboratories

class Store:
    def __init__(self):
        self.nurses        = Nurses()
        self.doctors       = Doctors()
        self.patients      = Patients()
        self.ampoules      = Ampoules()
        self.campaigns     = Campaigns()
        self.attendances   = Attendances()
        self.laboratories  = Laboratories()
