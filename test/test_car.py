import unittest
from datetime import datetime
# from engine.model.Engine
# from engine.model.calliope import Calliope

from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

# Tire Testing


class TestCarrigan(unittest.TestCase):
    def test_arrigan_should_be_serviced(self):
        tyre = Carrigan([1, 2, 3, 4])
        self.assertTrue(tyre.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_Octoprime_should_be_serviced(self):
        tyre = Octoprime([1, 2, 3, 4])
        self.assertTrue(tyre.needs_service())


# separate battery  Testing
class testSpindlerBattery(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


# Car model testing
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 10)
        current_mileage = 0
        last_service_mileage = 0
        tires = [1, 1, 1, 1]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire = [0, 0, 0, 0]

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage, tire)
        self.assertFalse(car.needs_service())
