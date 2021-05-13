from enum import Enum


class FlightStatus(Enum):
    ACTIVE, SCHEDULED, DELAYED, CANCELLED, DEPARTED, LANDED, IN_AIR, ARRIVED, UNKNOWN, DIVERTED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
