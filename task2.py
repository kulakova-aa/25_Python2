BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book


# TODO написать класс Library




class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Book: {self.name} (id={self.id}), pages: {self.pages}"

    def __repr__(self):
        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:
            return 1
        max_id = max(book.id for book in self.books)
        return max_id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        return -1


if __name__ == '__main__':
    empty_library = Library()  # пустая библиотека
    print(empty_library.get_next_book_id())  # Ожидается 1

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # библиотека с книгами
    print(library_with_books.get_next_book_id())  # Ожидается 3

    print(library_with_books.get_index_by_book_id(1))  # Ожидается 0 (индекс книги с id=1)