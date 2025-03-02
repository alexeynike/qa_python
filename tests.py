import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def create_books_collector(self):
        return BooksCollector()

    @pytest.fixture
    def create_book(self, create_books_collector):
        name = 'Война и мир'
        create_books_collector.add_new_book(name)
        return name

    def test_add_new_book_add_two_books(self, create_books_collector, create_book):

        create_books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(create_books_collector.get_books_genre()) == 2

    def test_set_book_genre_set_genre(self, create_books_collector, create_book):
        name = create_book
        genre = 'Детективы'
        create_books_collector.set_book_genre(name, genre)
        assert create_books_collector.get_book_genre(name) == genre

    def test_set_book_genre_without_genre(self, create_books_collector, create_book):
        name = create_book
        assert not create_books_collector.get_book_genre(name)

    def test_set_book_with_specific_genre(self, create_books_collector, create_book):
        name = create_book
        genre = 'Детективы'
        create_books_collector.set_book_genre(name, genre)
        assert len(create_books_collector.get_books_with_specific_genre(genre)) == 1

    def test_set_book_with_specific_genre_negative(self, create_books_collector, create_book):
        genre = 'Детективы'
        assert len(create_books_collector.get_books_with_specific_genre(genre)) == 0

    def test_get_books_genre_for_empty_books_genre(self,create_books_collector):
        assert len(create_books_collector.get_books_genre()) == 0

    def test_get_books_not_for_children(self, create_books_collector, create_book):
        book = create_book
        genre = 'Ужасы'
        create_books_collector.add_new_book('Test book')
        create_books_collector.set_book_genre(book, genre)
        create_books_collector.set_book_genre('Test book', 'Мультфильмы')
        assert len(create_books_collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_book(self, create_books_collector, create_book):
        book = create_book
        create_books_collector.add_book_in_favorites(book)
        assert len(create_books_collector.favorites) == 1

    def test_add_book_in_favorites_check_default(self, create_books_collector, create_book):
        assert len(create_books_collector.favorites) == 0

    def test_delete_book_from_favorites(self, create_books_collector, create_book):
        book = create_book
        create_books_collector.add_book_in_favorites(book)
        create_books_collector.delete_book_from_favorites(book)
        assert len(create_books_collector.favorites) == 0

    def test_get_list_of_favorites_books_get_favorites(self, create_books_collector, create_book):
        book = create_book
        create_books_collector.add_book_in_favorites(book)
        assert create_books_collector.get_list_of_favorites_books() == [book]