from .Flight import Flight


class Aircraft:
    def __init__(self, model: str, manufacturingYear: int, name: str):
        self.__name = name
        self.__model = model
        self.__manufacturingYear = manufacturingYear
        self.__seats = []

    def getFlights(self) -> list[Flight]:
        pass
