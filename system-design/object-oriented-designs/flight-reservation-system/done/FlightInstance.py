class FlightInstance:
    def __init__(self, gateNumber, deaprtureTime, status, aircraft):
        self.gateNumber = gateNumber
        self.__deaprtureTime = deaprtureTime
        self.__status = status
        self.__aircraft = aircraft

    def cancelFlight(self) -> bool:
        None

    def updateStatus(self, status):
        None
