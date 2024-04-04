from models import load_books, load_users, save_books, save_users

def load_data():
    """
    Loads the books and users from the JSON files.

    Returns:
        tuple: A tuple containing a list of book objects and a list of user objects.
    """
    return load_books(), load_users()

def save_data(books, users):
    """
    Saves the books and users to the JSON files.

    Args:
        books (list): A list of book objects.
        users (list): A list of user objects.
    """
    save_books(books)
    save_users(users)