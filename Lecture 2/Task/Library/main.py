from db import *
from library import library

def main():
    Seneca_Library = library("Seneca")

    Seneca_Library.add_book(("The Great Gatsby", "F. Scott Fitzgerald", "1925", "9780743273565"))
    Seneca_Library.add_book(("To Kill a Mockingbird", "Harper Lee", "1960", "9780061120084"))
    Seneca_Library.add_book(("1984", "George Orwell", "1949", "9780451524935"))
    Seneca_Library.add_book(("Pride and Prejudice", "Jane Austen", "1813", "9780679783268"))

    # Student borrow some book
    Seneca_Library.remove_book(("The Great Gatsby", "F. Scott Fitzgerald", "1925", "9780743273565"))
    
    # Search for a book by title
    print(Seneca_Library.search_by_title("1984"))

    # Search for a book by author
    print(Seneca_Library.search_by_author("Harper Lee"))

    # Library Close
    Seneca_Library.write_to_db()

if __name__ == "__main__":
    main()