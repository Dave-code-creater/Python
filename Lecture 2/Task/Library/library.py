from db import *

class library():
    """
    A class to represent a library.
    """

    def __init__(self, name: str):
        """
        Construct a library with a name and an empty book list.
        """
        self.name = name
        self.books = []
        self.conn = create_connection("library.db")


    # TODO: Add a book to the library
    def add_book(self, book: tuple):
        pass

    # TODO: Remove a book from the library
    def remove_book(self, book: tuple):
        pass 

    # TODO: Search for a book by title
    def search_by_title(self, title: str):
        pass 

    # TODO: Search for a book by author
    def search_by_author(self, author: str):
        pass 

    # TODO: Search for a book by published date
    def search_by_published_date(self, published_date: str):
        pass 

    # TODO: Search for a book by ISBN
    def search_by_isbn(self, isbn: str):
        pass 

    def write_to_db(self):
        """
        Write the books in the library to the database.
        """

        for book in self.books:
            insert_book(self.conn, book)

    def __str__(self) -> str:
        return f"Library {self.name} has {len(self.books)} books"
    
    
    def read_from_db(self):
        self.books = select_all_books(self.conn)
