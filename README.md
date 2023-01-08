<h1 align="center"> Custom LinkedIn Messaging </h1> <br>
<p align="center">
  <a>
    <img alt="Custom LinkedIn Messaging" title="Custom LinkedIn Messaging" src="https://github.com/agusticonesagago/linkedin_automation/blob/main/doc/images/example.png?raw=true" width="900" height="500">
  </a>
</p>

<p align="center">
  A tool for creating custom LinkedIn messages on the go, built with Python and FastAPI.
</p>


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
    - [Curl](#curl)
    - [Postman](#postman)
- [Example](#example)
- [Feedback](#feedback)
- [License](#license)

## Introduction

Revolutionize your recruitment process with this cutting-edge proof of concept! Building upon the LinkedIn [scraping project](https://github.com/python-scrapy-playbook/linkedin-python-scrapy-scraper) by [josephkearney91](https://github.com/josephkearney91), this tool leverages the power of the OpenAI API (Chat GPT) to send personalized messages to potential candidates in multiple languages. By scraping information from LinkedIn profiles, we can tailor the messages to better match the individual and stand out from the rest. Elevate your outreach strategy with targeted and individualized messages.

## Features

The following are some of the key features of this project:
- Personalized messages for each specific job opening can be created by making API requests with different job descriptions.
- API requests with different candidates in mind allow for the creation of tailored messages for each individual.
- Improve communication with the ability to send messages in different languages, reaching a wider audience.
- Scrape information from LinkedIn profiles to create customized messages for each candidate, increasing the chances of catching their attention.

## Getting Started

Before you can start using this project, there are a few steps you need to take to set it up:

1. Obtain API keys for ScrapeOps Proxy and OpenAI. These keys will allow you to access the necessary services and use the project.
    1. To obtain API key for ScrapeOps Proxy you need to go to the [ScrapeOps website](https://www.scrapeops.com/) and [sign up for a free API key here](https://scrapeops.io/app/register/main). The free plan allows for up to 1,000 requests per month. However, the service can also be easily scaled up to handle millions of pages per month if needed.

    2. To get an API key for OpenAI, go to the [OpenAI website](https://beta.openai.com/) and click on the "Sign Up" button. Once you have created an account, click on the "API" tab in the top menu, scroll down to the "Get started with the API" section, and click on the "Get API Key" button. Follow the prompts to create a new API key.

2. To use the API keys in this project, open the `.env` file in a text editor and replace "your_api_key" in the second line with the API key you obtained from ScrapeOps. The line should now read `SCRAPEOPS_API_KEY = "your_api_key"`. In addition to that, you also need to replace "your_api_key" in the first line with the API key you obtained from OpenAI. The line should now read `GPT_API_KEY = "your_key"`. Save the `.env` file. The `.env` file is used to store sensitive information, such as API keys, that should not be shared publicly. By placing the API keys in this file, you can use them in the project without exposing them to others.

3. To build the Docker image for this project, you will need to the following command: `docker-compose build`. This command should be run in the root directory of the project. It will create a Docker image that contains all the necessary components and dependencies for the project. 

4. To launch the project, run the command `docker-compose up` in the terminal, in the root directory of the project. This will start the Docker container and make the project available for use. The application will be running on port 5000. Once the container is running, the project will be ready for use.

## Usage
This project can be used in two ways: by using the `curl` command in the terminal or by installing Postman and making requests through the Postman interface.

### Curl

To use the `curl` command, you will need to enter the endpoint URL and any necessary parameters in the command line. 

For example, to make a POST request to the `http://127.0.0.1:5000/create` endpoint using `curl`, you might use a command like this: 

```
curl -X POST -d '{"user":"agustí-conesa-45288b167","job_description":"Company X seeks a mid to senior Python engineer who will participate in all aspects of architecting and developing new and innovative web applications. You will have the opportunity to work on cutting-edge technology and new product development in an established company that is rapidly growing. This is a great opportunity for an engineer looking to expand their well-established career, who is excited about search, solving complex problems, ownership, and who enjoys working with technologies like Python, Elasticsearch, GraphQL, AWS, and Frameworks like Django.You must be based in Spain and be eligible for employment within the EU, as X does not sponsor employment visa processes for this role.","language":"english"}' http://127.0.0.1:5000/create
```

### Postman
To make a POST request to the `http://127.0.0.1:5000/create` endpoint using Postman, follow these steps:

1. Install Postman:
    * Go to the Postman website
    * Click on the "Download" button
    * Follow the prompts to install Postman on your computer
2. Open Postman.
3. Select the POST method from the dropdown menu.
4. Enter the endpoint `http://127.0.0.1:5000/create` in the address bar.
5. In the body of the request, select the "raw" option and choose "JSON" as the type.
6. Enter the following JSON object in the body of the request, replacing the values with your own:

```
{
    "user": "agustí-conesa-45288b167",
    "job_description": "Company X seeks a mid to senior Python engineer who will participate in all aspects of architecting and developing new and innovative web applications. You will have the opportunity to work on cutting-edge technology and new product development in an established company that is rapidly growing. This is a great opportunity for an engineer looking to expand their well-established career, who is excited about search, solving complex problems, ownership, and who enjoys working with technologies like Python, Elasticsearch, GraphQL, AWS, and Frameworks like Django.You must be based in Spain and be eligible for employment within the EU, as X does not sponsor employment visa processes for this role.",
    "language": "english"
}
```

## Example
Here is an example of how to make a POST request to the `http://127.0.0.1:5000/create` endpoint using Postman:

<a>
  <img alt="Example of Postman" title="Commits" src="https://github.com/agusticonesagago/linkedin_automation/blob/main/doc/images/short_message.png?raw=true" width="900" height="500">
</a>

To make this request, you will need to enter the following information:

* **User**: This is the identifier of the LinkedIn profile that you want to create the custom message for. For example, if the LinkedIn profile you want is `https://www.linkedin.com/in/agustí-conesa-45288b167/`, the user value would be `agustí-conesa-45288b167`.

* **Job Description**: This is the text of the job description you want to use. You can enter any job description you want.

* **Language**: This is the language you want the text to be generated in. You can enter any language you want.


## Feedback

Our project on customizing LinkedIn messages is constantly evolving, and we welcome any feedback or suggestions to improve the tool. If you have any ideas on how we can make the tool more useful or efficient, we would love to hear from you! You can reach out to us through email or by submitting a pull request with your proposed changes. We value the input of our users and are always looking for ways to improve the tool. Don't hesitate to contact us and let us know what you think!

## License

This project is licensed under the Creative Commons Attribution 4.0 license, which allows others to use and modify the code as long as proper attribution is given. If you use this project in your work, please make sure to include a reference to this repository and its creators.