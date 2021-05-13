from .Person import Person


class Customer(Person):
    def __init__(self, frequent_flyer):
        self.frequent_flyer = frequent_flyer

    def get_itenaries(self):
        None
       