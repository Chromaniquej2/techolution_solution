import json
import sys

from check import check_out, check_in
from models import load_books, load_users, save_books, save_users
from user import User

def add_book(books, title, author, isbn):
    """
    Adds a book to the list of books.

    Args:
        books (list): A list of book objects.
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
    """
    books.append(Book(title, author, isbn, True))

def update_book(books, book_index, title, author, isbn):
    """
    Updates a book in the list of books.

    Args:
        books (list): A list of book objects.
        book_index (int): The index of the book to update.
        title (str): The new title of the book.
        author (str): The new author of the book.
        isbn (str): The new ISBN of the book.
    """
    books[book_index] = Book(title, author, isbn, books[book_index].availability)

def delete_book(books, book_index):
    """
    Deletes a book from the list of books.

    Args:
        books (list): A list of book objects.
        book_index (int): The index of the book to delete.
    """
    del books[book_index]

def list_books(books):
    """
    Lists the books.

    Args:
        books (list): A list of book objects.
    """
    for i, book in enumerate(books):
        print(f"{i}: {book.title} by {book.author} (ISBN: {book.isbn}, {book.availability})")

def search_books(books, keyword):
    """
    Searches for books based on a keyword.

    Args:
        books (list): A list of book objects.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of book objects that match the keyword.
    """
    results = [i for i, book in enumerate(books) if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
    return results

def add_user(users, name, user_id):
    """
    Adds a user to the list of users.

    Args:
        users (list): A list of user objects.
        name (str): The name of the user.
        user_id (str): The user ID of the user.
    """
    users.append(User(name, user_id))

def update_user(users, user_index, name, user_id):
    """
    Updates a user in the list of users.

    Args:
        users (list): A list of user objects.
        user_index (int): The index of the user to update.
        name (str): The new name of the user.
        user_id (str): The new user ID of the user.
    """
    users[user_index] = User(name, user_id)

def delete_user(users, user_index):
    """
    Deletes a user from the list of users.

    Args:
        users (list): A list of user objects.
        user_index (int): The index of the user to delete.
    """
    del users[user_index]

def list_users(users):
    """
    Lists the users.

    Args:
        users (list): A list of user objects.
    """
    for i, user in enumerate(users):
        print(f"{i}: {user.name} ({user.user_id})")

def search_users(users, keyword):
    """
    Searches for users based on a keyword.

    Args:
        users (list): A list of user objects.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of user objects that match the keyword.
    """
    results = [i for i, user in enumerate(users) if keyword.lower() in user.name.lower()]
    return results

def main():
    """
    The main function of the library management system.
    """
    books, users = load_data()
    while True:
        command = input("Enter a command (add/update/delete/list/search/checkout/checkin/exit): ").split()
        if len(command) == 0:
            continue

        if command[0] == "add":
            if command[1] == "book":
                title, author, isbn = input("Enter book details (title, author, isbn): ").split()
                add_book(books, title, author, isbn)
                save_data(books, users)
            elif command[1] == "user":
                name, user_id = input("Enter user details (name, user_id): ").split()
                add_user(users, name, user_id)
                save_data(books, users)

        elif command[0] == "update":
            if command[1] == "book":
                book_index, title, author, isbn = map(int, input("Enter book details (index, title, author, isbn): ").split())
                update_book(books, book_index, title, author, isbn)
                save_data(books, users)
            elif command[1] == "user":
                user_index, name, user_id = map(int, input("Enter user details (index, name, user_id): ").split())
                update_user(users, user_index, name, user_id)
                save_data(books, users)

        elif command[0] == "delete":
            if command[1] == "book":
                book_index = int(input("Enter book index: "))
                delete_book(books, book_index)
                save_data(books, users)
            elif command[1] == "user":
                user_index = int(input("Enter user index: "))
                delete_user(users, user_index)
                save_data(books, users)

        elif command[0] == "list":
            if command[1] == "books":
                list_books(books)
            elif command[1] == "users":
                list_users(users)

        elif command[0] == "search":
            if command[1] == "books":
                keyword = input("Enter keyword: ")
                results = search_books(books, keyword)
                for i, index in enumerate(results):
                    print(f"{i}: {books[index].title} by {books[index].author} (ISBN: {books[index].isbn}, {books[index].availability})")
            elif command[1] == "users":
                keyword = input("Enter keyword: ")
                results = search_users(users, keyword)
                for i, index in enumerate(results):
                    print(f"{i}: {users[index].name} ({users[index].user_id})")

        elif command[0] == "checkout":
            book_index = int(input("Enter book index: "))
            user_index = int(input("Enter user index: "))
            check_out(books[book_index], users[user_index])
            save_data(books, users)

        elif command[0] == "checkin":
            book_index = int(input("Enter book index: "))
            user_index = int(input("Enter user index: "))
            check_in(books[book_index], users[user_index])
            save_data(books, users)

        elif command[0] == "exit":
            sys.exit(0)

if __name__ == "__main__":
    main()