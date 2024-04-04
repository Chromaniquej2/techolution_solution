from models import load_books, save_books

def check_out(book, user):
    """
    Checks out a book for a user.

    Args:
        book (Book): The book to check out.
        user (User): The user to check out the book for.
    """
    books = load_books()
    book.availability = False
    save_books(books)

def check_in(book, user):
    """
    Checks in a book for a user.

    Args:
        book (Book): The book to check in.
        user (User): The user to check in the book for.
    """
    books = load_books()
    book.availability = True
    save_books(books)