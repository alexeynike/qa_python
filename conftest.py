import pytest

from main import BooksCollector

@pytest.fixture
def create_books_collector():
    return BooksCollector()


@pytest.fixture
def create_book(create_books_collector):
    name = 'Война и мир'
    create_books_collector.add_new_book(name)
    return name