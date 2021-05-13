from enum import Enum


class ReservationStatus(Enum):
    CONFIRMED, PAID, UNPAID, CANCELLED, ABANDONED, CHECKED_IN, PENDING, REQUESTED = 1, 2, 3, 4, 5, 6, 7, 8
