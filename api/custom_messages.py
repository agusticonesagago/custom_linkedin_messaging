"""This module writes custom LinkedIn messages based on a vacancy description.

Uses OpenAI to generate personalized messages tailored to the vacancy's
requirements and responsibilities. Messages highlight relevant skills and
experience and encourage recipient to be considered for the role.
To use the module, provide vacancy description and LinkedIn profile as input.
Optionally specify a language for the message.
"""
from .controllers import openai, rapidapi


def main(user: str, job_description: str, language: str) -> dict[str, str]:
    """Creates custom LinkedIn messages based on the user's input and job description.

    Args:
        user: The LinkedIn user for whom the message is being generated.
        job_description: The description of the job for which the message is generated.
        language: The language in which the message should be written.

    Returns:
        A customized LinkedIn message based on the input data.
    """
    candidate = rapidapi.get_linkedin_profile(user).json()["data"]

    candidate_info = {
        "current_position": candidate["job_title"],
        "about": candidate["about"],
        "name": candidate["full_name"],
        "location": candidate["location"].split(",")[0],
    }
    current_experience = candidate["experiences"][0]
    previous_experience = candidate["experiences"][1]

    prompt = (
        f"Write a message in {language} to {candidate_info['name']} to offer a vacancy "
        f"to this position description: '{job_description} '. This candidate is currently "
        f"working as {candidate_info['current_position']} and describes himself as "
        f"'{candidate_info['about']}'. In addition to that, this candidate lives nowadays in "
        f"{candidate_info['location']}. This candidate has experience working with "
        f"{current_experience['description']} in the company of {current_experience['company']} and also "
        f"has experience with {previous_experience['description']} in the company of "
        f"{previous_experience['company']}. Try to write a message in {language} to get their attention, "
        "trying to match his/here work experience with the job description mentioned."
    )

    response = openai.generate_message(prompt)

    return {"message": response.json()["choices"][0]["text"]}
