class Book:
    """
    Represents a book in the library management system.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        availability (bool): The availability of the book.
    """

    def __init__(self, title, author, isbn, availability):
        """
        Initializes a new book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            availability (bool): The availability of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def __repr__(self):
        """
        Returns a string representation of the book object.

        Returns:
            str: A string representation of the book object.
        """
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.availability})"