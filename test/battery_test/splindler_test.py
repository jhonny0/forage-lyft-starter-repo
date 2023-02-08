import unittest
from datetime import datetime
from battery.splindler import SpindlerBattery


class SplinderTest (unittest.TestCase):
    def test_need_service_true(self):
        current_date = datetime.fromisoformat("2023-02-08")
        last_service_date = datetime.fromisoformat("2021-01-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.nedd_service())

    def test_need_service_false(self):
        current_date = datetime.fromisoformat("2023-02-08")
        last_service_date = datetime.fromisoformat("2022-02-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.nedd_service())