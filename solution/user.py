class User:
    """
    Represents a user in the library management system.

    Attributes:
        name (str): The name of the user.
        user_id (str): The user ID of the user.
    """

    def __init__(self, name, user_id):
        """
        Initializes a new user object.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        """
        Returns a string representation of the user object.

        Returns:
            str: A string representation of the user object.
        """
        return f"User('{self.name}', '{self.user_id}')"