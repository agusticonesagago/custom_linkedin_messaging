"""Module for interacting with the RapidAPI to retrieve LinkedIn profile data."""
import requests

from api.exceptions.rapidapi import RapidAPIException
from api.clients import rapidapi


def get_linkedin_profile(user: str, include_skills: bool = False) -> requests.Response:
    """Retrieves LinkedIn profile data from RapidAPI.

    Args:
        user: The LinkedIn user whose information will be retrieved.
        include_skills: Whether to include skills in the profile data.

    Returns:
        requests.Response: A `Response` object containing the response from the RapidAPI.

    Raises:
        RapidAPIException: If an error occurs while retrieving the LinkedIn profile.
    """
    try:
        return rapidapi.get_linkedin_profile(
            f"https://www.linkedin.com/in/{user}/", include_skills
        )
    except requests.exceptions.HTTPError as http_error:
        raise RapidAPIException(
            "An error occurred while retrieving LinkedIn profile."
        ) from http_error
