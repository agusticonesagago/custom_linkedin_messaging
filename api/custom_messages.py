"""This module writes custom LinkedIn messages based on a vacancy description.

Uses OpenAI to generate personalized messages tailored to the vacancy's
requirements and responsibilities. Messages highlight relevant skills and
experience and encourage recipient to be considered for the role.
To use the module, provide vacancy description and LinkedIn profile as input.
Optionally specify a language for the message.
"""
import subprocess
import json

from .controllers import openai


def _get_company_name(url: str) -> str:
    """Extract the company name from a LinkedIn company URL.

    Args:
        url: The LinkedIn company URL from which to extract the company name.

    Returns:
        The company name.
    """
    return url.rsplit("/", 1)[-1].replace("-", " ").title()


def main(user: str, job_description: str, language: str)  -> dict[str, str]:
    """Creates custom LinkedIn messages based on the user's input and job description.

    Args:
        user: The LinkedIn user for whom the message is being generated.
        job_description: The description of the job for which the message is generated.
        language: The language in which the message should be written.

    Returns:
        A customized LinkedIn message based on the input data.
    """
    subprocess.run(
        [
            "scrapy",
            "crawl",
            "linkedin_people_profile",
            "-a",
            f"profile={user}",
            "-O",
            "profile.json",
        ],
        check=True
    )

    with open("profile.json", encoding="utf-8") as file:
        data = json.load(file)

    candidate = data[0]
    candidate_info = {
        "current_position": candidate["description"],
        "about": candidate["about"],
        "name": candidate["name"],
        "location": candidate["location"].split(",")[0],
    }
    current_experience = candidate["experience"][0]
    current_company = _get_company_name(
        candidate["experience"][0]["organisation_profile"]
    )
    previous_experience = candidate["experience"][1]
    previous_company = _get_company_name(
        candidate["experience"][1]["organisation_profile"]
    )

    prompt = (
        f"Write a message in {language} to {candidate_info['name']} to offer a vacancy "
        f"to this position description: '{job_description} '. This candidate is currently "
        f"working as {candidate_info['current_position']} and describes himself as "
        f"'{candidate_info['about']}'. In addition to that, this candidate lives nowadays in "
        f"{candidate_info['location']}. This candidate has experience working with "
        f"{current_experience['description']} in the company of {current_company} and also "
        f"has experience with {previous_experience['description']} in the company of "
        f"{previous_company}. Try to write a message in {language} to get their attention, "
        "trying to match his/here work experience with the job description mentioned."
    )

    response = openai.generate_message(prompt)
    subprocess.run(
        ["rm", "profile.json"],
        check=True
    )

    return {"message": response.json()["choices"][0]["text"]}
