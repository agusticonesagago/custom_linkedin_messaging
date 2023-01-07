"""This module provides custom exceptions for the OpenAI.

Handles specific error scenarios such as invalid input,
authentication errors, and resource not found errors.
Includes error message and code for identification and handling.
Import exceptions from the module and raise them when appropriate.
Implement exception handling logic to handle error scenarios and provide
an appropriate response to the user.

For example:
try:
    # Code that may raise an exception
except OpenAIError as e:
    # Handle the exception
The OpenAIError class is the base class for all custom exceptions.
Catch specific exceptions individually or use OpenAIError to catch any.
"""


class OpenAIException(Exception):
    """Custom exception for OpenAI errors."""
    def __init__(self, message: str):
        """Initializes a new instance of the exception.

        Args:
            message: The error message associated with the exception.
        """
        self.message = message
