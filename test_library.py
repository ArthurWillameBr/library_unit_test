import pytest
from library import Library, Book
from exceptions import BookError, CopyError

def test_create_library():
    library = Library()
    assert library.books == []
    assert library.copies == []

def test_add_valid_book():
    library = Library()
    book = library.add_book("Livro teste", "Editora teste", ["Arthur", "Pedro"])
    assert book.title == "Livro teste"
    assert book.publisher == "Editora teste"
    assert len(book.authors) == 2

def test_add_book_no_authors():
    library = Library()
    with pytest.raises(BookError) as error:
        library.add_book("Livro teste", "Editora teste", [])
    assert str(error.value) == "Deve haver ao menos um autor."

def test_add_valid_copy():
    library = Library()
    book = library.add_book("Livro teste", "Editora teste", ["Arthur", "Pedro"])
    copy = library.add_copy(book, 2024, 17, 221)
    assert copy.year == 2024
    assert copy.edition == 17
    assert copy.pages == 221

def test_add_copy_invalid_year():
    library = Library()
    book = library.add_book("Livro teste", "Editora teste", ["Arthur"])
    with pytest.raises(CopyError) as error:
        library.add_copy(book, -2024, 17, 224)
    assert str(error.value) == "O ano de publicação deve ser positivo."