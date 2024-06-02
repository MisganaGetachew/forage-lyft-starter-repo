from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        print("Yes it needs service")


class otherCar(Car):

    def needs_service(self):
        print("This is a subclass method!")


c = otherCar(12)

c.needs_service()

print("hello")
