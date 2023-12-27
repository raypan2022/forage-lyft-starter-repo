import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class TestEngine(unittest.TestCase): 
  def test_capulet_service_true(self):
    last_service_mileage = 0
    current_mileage = 30001
    engine = CapuletEngine(last_service_mileage, current_mileage)
    self.assertTrue(engine.needs_service())
  
  def test_capulet_service_false(self):
    last_service_mileage = 0
    current_mileage = 1000
    engine = CapuletEngine(last_service_mileage, current_mileage)
    self.assertFalse(engine.needs_service())
  
  def test_willoughby_service_true(self):
    last_service_mileage = 0
    current_mileage = 60001
    engine = WilloughbyEngine(last_service_mileage, current_mileage)
    self.assertTrue(engine.needs_service())
  
  def test_willoughby_service_false(self):
    last_service_mileage = 0
    current_mileage = 35000
    engine = WilloughbyEngine(last_service_mileage, current_mileage)
    self.assertFalse(engine.needs_service())
  
  def test_sternman_service_true(self):
    warning_light_is_on = True
    engine = SternmanEngine(warning_light_is_on)
    self.assertTrue(engine.needs_service())
  
  def test_sternman_service_false(self):
    warning_light_is_on = False
    engine = SternmanEngine(warning_light_is_on)
    self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
