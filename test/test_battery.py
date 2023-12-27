import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestBattery(unittest.TestCase) : 
  def test_spindler_service_true(self):
    current_date = date.fromisoformat("2023-01-01")
    last_service_date = date.fromisoformat("2020-01-01")
    battery = SpindlerBattery(last_service_date, current_date)
    self.assertTrue(battery.needs_service())

  def test_spindler_service_false(self):
    current_date = date.fromisoformat("2023-01-01")
    last_service_date = date.fromisoformat("2022-01-01")
    battery = SpindlerBattery(last_service_date, current_date)
    self.assertFalse(battery.needs_service())
  
  def test_nubbin_service_true(self):
    current_date = date.fromisoformat("2023-01-01")
    last_service_date = date.fromisoformat("2018-01-01")
    battery = NubbinBattery(last_service_date, current_date)
    self.assertTrue(battery.needs_service())

  def test_nubbin_service_false(self):
    current_date = date.fromisoformat("2023-01-01")
    last_service_date = date.fromisoformat("2020-01-01")
    battery = NubbinBattery(last_service_date, current_date)
    self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
