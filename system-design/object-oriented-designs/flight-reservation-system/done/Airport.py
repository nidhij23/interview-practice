from .Address import Address
from .Flight import Flight


class Airport:
    def __init__(self, name: str, address: Address, code: int):
        self.__name = name
        self.__address = address
        self.__code = code

    def getFlights(self, code: int) -> list[Flight]:
        """returns a list of objects of type FLight"""
        pass
