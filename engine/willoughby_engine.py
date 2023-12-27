from .engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.__warning_light_is_on
