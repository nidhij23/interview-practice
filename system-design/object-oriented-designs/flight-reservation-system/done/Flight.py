from .FlightInstance import FlightInstance


class Flight:
    def __init__(self, flight_number: int, name: str, departureAirport: str, arrivalAirport: str, duration: int):
        self.__name = name
        self.__departureAirport = departureAirport
        self.__arrivalAirport = arrivalAirport
        self.__duration = duration
        self.__flight_number = flight_number
        self.__weeklySchedules = []
        self.__custom_schedules = []
        self.__flight_instances = []



    def addFlightSchedule(self) -> bool:
        pass

    def getFlightInstance(self) -> list[FlightInstance]:
        pass
