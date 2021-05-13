from enum import Enum
from abc import ABC, abstractmethod


class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Address:
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Book(ABC):
    def __init__(self, id, title, subject, publication, language, number_of_pages):
        self.__id = id
        self.__title = title
        self.__subject = subject
        self.__publication = publication
        self.__author = []
        self.__language = language
        self.__number_of_pages = number_of_pages


class BookItem(Book):
    def __init__(self, barcode, is_refernce_only, borrowed, du_date, price, format, status, date_purchse,
                 publication_date, placed_at):

        def checkout(self, memberid):
            if self.is_refernce_only():
                return False

            if not BookLending.lend_book(self.barcode):
                return False
            self.update_book_item_status(BookStatus.LOANEd)
            return True


class Rack:
    def __init__(self, number, loation_identifier):   pass


class Search(ABC):
    def search_by_title(self):
        def search_by_suthor():  pass

        def seacrh_bycategory():     pass

        def search_by_pub_date():        pass


class Catalog(Search):
    def __init__(self):
        self.__book_title = {}
        self.__bookt_authors = {}
        self.__boook_subjects = {}
        self.__book_publicate_dates = {}

    def search_by_suthor(self, query):
        return self.__bookt_authors.get(query)


class BookReservation:
    def __init__(self, creation_date, status, book_item, barcode, member_id):
        def fetch_reservation_detail(self, barcode):


class BookLending:
    def __init(self, cretoin_id, barcode, member_id, status, due_date):
        pass

    def lend_book(self):
        None

    def fetchBookLendingDetails(self, barcode, memberid):
        pass


class Fine:
    def __init__(self, creationdate, barcode, memberid): None

    def collectFine(self, memberid, days): None


class Account(ABC):
    def __init__(self, password, id, phone, person, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status
        self.person = person

    def reset_password(self): pass


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        super().__init__(id, password, person, status)

    def add_books(self, bookitem): pass

    def remove_book(self, bookitem): pass

    def block_member(self, memberid): pass


class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.Active):
        super().__init__(id, password, person, status)
        self._date_of_membership = datetime.date.today()
        self.__total_books_checkout = 0

    def get_books_checkout(self): pass

    def reserveboook(self): pass

    def returnbook(self): pass

    def check_for_fine(self): pass

    def return_boook_item(self):     pass


class BookFormat(Enum):
    HARDCOVER, MAGAZINE, AUDIO_BOOK, EBOOK, JOURNAL = 1, 2, 3, 4, 5


class BookSTatus(Enum):
    AVAILABLE, LOANED, RESERVED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
    WAITING, PENDING, CANCELLED, NONE = 1, 2, 3, 4


class AccountStatus(Enum):
    ACTIVE, BLOCKED, CLOSED, BLACKLISTED = 1, 2, 3, 4


class Person(ABC):
    def __init__(self, name, address, email, phone):
        pass


class Constants:
    self.MAX_BOOKS_ISSUED_TO_A_USER = 5
    self.MA_LENDING_DAYS = 10
