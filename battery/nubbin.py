from battery.battery import Battery 
from util import add_years_to_date


class NubbinBattery (Battery):
    def __init__(self, current_date, last_service_date) :
        self.current_date = current_date 
        self.last_service_date = last_service_date

    def nedd_service(self):
        next_battery_service = add_years_to_date(self.last_service_date ,4)
        if next_battery_service < self.current_date:
            return True
        else:
            return False 