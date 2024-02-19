"""Module that provides custom exceptions for RapidAPI."""


class RapidAPIException(Exception):
    """Custom exception for Rapid API errors."""

    def __init__(self, message: str):
        """Initializes a new instance of the exception.

        Args:
            message: The error message associated with the exception.
        """
        self.message = message
