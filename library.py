from exceptions import BookError, CopyError

class Book:
    def __init__(self, title, publisher, authors):
        if not title:
            raise BookError("O título do livro não pode ser vazio.")
        if not publisher:
            raise BookError("A editora não pode ser vazio.")
        if not authors or len(authors) == 0:
            raise BookError("Deve haver ao menos um autor.")  

        self.title = title
        self.publisher = publisher
        self.authors = authors

class Copy:
    def __init__(self, book, year, edition, pages):
        if not isinstance(book, Book):
            raise CopyError("O exemplar deve estar associado a um livro.")
        if year <= 0:
            raise CopyError("O ano de publicação deve ser positivo.")
        if edition <= 0:
            raise CopyError("A edição deve ser positiva.")
        if pages <= 0:
            raise CopyError("A quantidade de páginas deve ser positiva.")
        
        self.book = book
        self.year = year
        self.edition = edition
        self.pages = pages

class Library:
    def __init__(self):
        self.books = []
        self.copies = []

    def add_book(self, title, publisher, authors):
        book = Book(title, publisher, authors)
        self.books.append(book)
        return book

    def add_copy(self, book, year, edition, pages):
        copy = Copy(book, year, edition, pages)
        self.copies.append(copy)
        return copy

