
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):

        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()

    # def engine(self) -> Engine:
    #     if self.engine == "capulet_engine ":
    #         return capulet_engine()
    #     elif self.engine == "sternman_engine":
    #         return sternman_engine()
    #     elif self.engine == "willoughby_engine":
    #         return willoughby_engine()

    # def battery(self) -> Battery:
    #     return Battery()

    # def needs_service(self):
    #     pass
