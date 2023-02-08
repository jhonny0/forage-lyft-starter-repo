import unittest
from datetime import datetime
from battery.nubbin import NubbinBattery


class NubbinTest (unittest.TestCase):
    def test_need_service_true(self):
        current_date = datetime.fromisoformat("2023-02-08")
        last_service_date = datetime.fromisoformat("2018-02-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.nedd_service())

    def test_need_service_false(self):
        current_date = datetime.fromisoformat("2023-02-08")
        last_service_date = datetime.fromisoformat("2022-02-15")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.nedd_service())