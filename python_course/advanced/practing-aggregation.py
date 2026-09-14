class Bookshelf:
    def __init__(self):
        self._books = []

    def insert_books(self, *books):
        self._books += books

    def list_books(self):
        for book in self._books:
            print(f'Name: {book.name}\nGenre: {book.book_genre}')

class Book:
    def __init__(self, name, book_genre):
        self.name = name
        self.book_genre = book_genre

shelf = Bookshelf()
book1, book2 = Book('Harry Potter 1', 'Fantasy'), Book('Harry Potter 2', 'Fantasy')
shelf.insert_books(book1, book2)
shelf.list_books()