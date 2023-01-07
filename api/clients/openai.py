"""Module for generating completions using the OpenAI API.

This module contains a function for generating completions for a given prompt using the
OpenAI API. The completions are generated using the `text-davinci-002` model, with a
temperature of 0.5 and a maximum of 2048 tokens. The function returns the response from
the OpenAI API as a `Response` object.

The module includes the `completions` function, which takes a prompt as input and returns
the generated completions. If an error occurs while making the request to the OpenAI API,
the function may raise a `requests.HTTPError` with a specific error message and code. If
the request takes longer than the specified timeout, the function may raise a `Timeout`
error.

To use the module, import it and call the `completions` function with the desired prompt.
For example:

import openai_completions

response = openai_completions.completions('Generate completions for me.')
"""
import os
import requests

from dotenv import load_dotenv

def completions(prompt: str) -> requests.Response:
    """Generates completions for the given prompt using the OpenAI API.

    Args:
        prompt : The prompt for which to generate completions. This should be a brief
            statement or explanation that describes the context or topic for which completions
            are desired.

    Returns:
        requests.Response: A `Response` object containing the response from the OpenAI API.

    Raises:
        requests.HTTPError: If an error occurs while making the request to the OpenAI API.
        Timeout: If the request to the OpenAI API takes longer than the specified timeout.
    """
    load_dotenv()

    header = {
        "Authorization": f"Bearer {os.getenv('GPT_API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0.5,
    }

    response = requests.post(
        "https://api.openai.com/v1/completions", headers=header, json=data, timeout=300
    )
    response.raise_for_status()

    return response
