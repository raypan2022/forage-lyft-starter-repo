import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestTires(unittest.TestCase) : 
  def test_carrigan_service_true(self):
    tire_wear = [0.9, 0.1, 0.1, 0.1]
    tires = CarriganTires(tire_wear)
    self.assertTrue(tires.needs_service())

  def test_carrigan_service_false(self):
    tire_wear = [0.1, 0.1, 0.1, 0.1]
    tires = CarriganTires(tire_wear)
    self.assertFalse(tires.needs_service())
  
  def test_octoprime_service_true(self):
    tire_wear = [0.9, 0.9, 1, 1]
    tires = OctoprimeTires(tire_wear)
    self.assertTrue(tires.needs_service())

  def test_octoprime_service_false(self):
    tire_wear = [1, 0.1, 0.1, 0.1]
    tires = OctoprimeTires(tire_wear)
    self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
