from tire.tire import Tire


class Octoprime(Tire):

    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        return True if sum(self.tires) >= 3 else False
