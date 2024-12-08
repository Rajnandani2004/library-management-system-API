# models.py
from typing import List, Optional

class Book:
    def __init__(self, id: int, title: str, author: str, available: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

class Member:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
