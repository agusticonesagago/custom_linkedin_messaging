"""Module for interacting with the RapidAPI to retrieve LinkedIn profile data."""
import requests
import os
from typing import Union
from dotenv import load_dotenv


def get_linkedin_profile(
    linkedin_url: str, include_skills: bool = False
) -> Union[dict, None]:
    """Retrieves LinkedIn profile data from RapidAPI.

    Args:
        linkedin_url: The URL of the LinkedIn profile.
        include_skills: Whether to include skills in the profile data.

    Returns:
        requests.Response: A `Response` object containing the response from the Rapid API.

    Raises:
        requests.HTTPError: If an error occurs while making the request to the Rapid API.
    """
    load_dotenv()

    response = requests.get(
        "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile",
        headers={
            "X-RapidAPI-Key": os.environ.get("RAPID_API_KEY"),
            "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com",
        },
        params={
            "linkedin_url": linkedin_url,
            "include_skills": str(include_skills).lower(),
        },
    )

    response.raise_for_status()

    return response
