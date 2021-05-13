import datetime


class URL:
    originalURL: str
    creationDate: datetime
    expirationTime: datetime
    userID: int
    hash: str


class User:
    name: str
    userId: int
    emailId: str
    creationDate: datetime
    lastLogin: datetime
