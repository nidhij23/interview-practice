from enum import Enum


class PaymentStatus(Enum):
    UNPAID, PAID, CANCELLED, COMPLETED, REFUNDED, DECLINED, ABANDONED, SETTLED, FILLED, SETTLING = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
