from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name=name
        self.__address=address
        self.__email=email
        self.__phone=phone
        self.__account=account
        
