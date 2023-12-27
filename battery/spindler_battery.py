from .battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        return self.__last_service_date.replace(year=self.last_service_date.year + 4) < self.__current_date