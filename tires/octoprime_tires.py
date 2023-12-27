from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.__tire_wear = tire_wear

    def needs_service(self):
        return sum(self.__tire_wear) >= 3
