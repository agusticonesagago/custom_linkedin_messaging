"""Module for generating messages using the OpenAI client.

This module contains a controller for the OpenAI client that is used to generate customized
messages based on a given request or explanation. The messages are tailored to the specific
content of the request or explanation, and are designed to provide a clear and concise response.

The module includes the `generate_message` function, which takes a request or explanation as
input and returns a generated message. If an error occurs while generating the message, the
function may raise an `OpenAIException` with a specific error message and code.

To use the module, import it and call the `generate_message` function with the desired input.
For example:

import openai_controller

message = openai_controller.generate_message('Generate a message for me.')
"""
import requests

from api.exceptions.openai import OpenAIException
from api.clients import openai


def generate_message(request: str) -> requests.Response:
    """Generates a message based on the given request or explanation.

    Args:
        request: The request/explanation for which to generate a message.

    Returns:
        A message generated based on the input request/explanation.
    Raises:
        OpenAIException: If an error occurred while generating the message.
    """
    try:
        return openai.completions(request)
    except requests.exceptions.HTTPError as http_error:
        raise OpenAIException("An error occurred while generating message.") from http_error
