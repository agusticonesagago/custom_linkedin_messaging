"""API for generating custom messages for LinkedIn profiles.

This API provides an endpoint for generating custom messages for LinkedIn profiles based on a
description of a vacancy and a user's LinkedIn profile. The messages are generated using the
`custom_messages` module, which uses the OpenAI to generate personalized messages that are
tailored to the specific requirements and responsibilities of the vacancy. The messages are
designed to highlight the relevant skills and experiences of the LinkedIn user and encourage
the recipient to be considered for the role.

The API includes a `PromptRequest` model that defines the input data for the API endpoint,
and a `create` function that handles the request and generates the custom message. The `create`
function accepts a `PromptRequest` object as input and returns a JSON response containing the
generated message.
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .custom_messages import main

class PromptRequest(BaseModel): # pylint: disable=too-few-public-methods
    """Model for get the message prompt request.

    This model defines the data required for generating a LinkedIn message based on a job
    description and a user's LinkedIn profile. It consists of the following fields:

    Attributes:
        user: The LinkedIn profile of the user for whom the message will be generated.
        job_description: The description of the vacancy for which the message will be generated.
        language: The language in which the message will be generated.
    """
    user: str
    job_description: str
    language: str


app = FastAPI()


@app.post("/create")
def create(request: PromptRequest) -> JSONResponse:
    """Generates a custom message for a LinkedIn profile based on a job description.

    This function generates a custom message for a LinkedIn profile based on a job description
    and a user's LinkedIn profile. The message is generated using the `custom_messages` module,
    which uses the OpenAI to generate personalized messages that are tailored to the specific
    requirements and responsibilities of the vacancy. The messages are designed to highlight the
    relevant skills and experiences of the LinkedIn user and encourage the recipient to be
    considered for the role.

    Args:
        request: The request data for generating the message. This should be a
            `PromptRequest` object with the following fields:
            - `user`: The LinkedIn profile of the user for whom the message will be generated.
            - `job_description`: The description of the vacancy for which the message will be
              generated.
            - `language`: The language in which the message will be generated.

    Returns:
        A JSON response containing the generated message. The response has the following fields:
            - `message`: The generated message.
    """
    data = main(request.user, request.job_description, request.language)
    return JSONResponse(content=data, status_code=200)
