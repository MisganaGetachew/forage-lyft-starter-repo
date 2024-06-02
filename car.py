from abc import ABC, abstractmethod
from engine.Engine import Engine
from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import Battery


class Servicable(ABC):

    @abstractmethod
    def needs_service(self):
        pass


class Car(Servicable):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine

    def engine(self) -> Engine:
        if self.engine == "capulet_engine ":
            return capulet_engine()
        elif self.engine == "sternman_engine":
            return sternman_engine()
        elif self.engine == "willoughby_engine":
            return willoughby_engine()

    def battery(self) -> Battery:
        return Battery()

    def needs_service(self):
        pass
