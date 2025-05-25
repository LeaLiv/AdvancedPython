from operator import truediv

import pytest

from book import Book
from library import Library

@pytest.fixture()
def library():
    return Library()

def test_add_book_success(library):
    library.add_book(Book("some","someone"))
    assert len(library.books)==1
    assert library.books[0]

def test_add_user(library):
    library.add_user("lea")
    assert len(library.users)==1
    assert library.users[0]

def test_check_out_book_user_not_registered(library):
    book=Book("some","some")
    with pytest.raises(ValueError):
        library.check_out_book("s",book)

def test_return_book(library):
    book=Book("some","some")
    library.add_book(book)
    library.add_user("s")
    with pytest.raises(ValueError,match=f"Book '{book.title}' by {book.author} was not checked out by 's'."):
        library.return_book("s",book)

def test_search_books(library):
    book=Book("some","some")
    library.add_book(book)
    find_book=library.search_books("SoMe")
    assert find_book

def test_check_out_book_not_in_library(library):
    library.add_user("s")
    book=Book("some","some")
    with pytest.raises(ValueError,match=f"Book '{book.title}' by {book.author} is not in the library."):
        library.check_out_book("s",book)

def test_valid_value(library):
    with pytest.raises(ValueError):
        library.add_user("")