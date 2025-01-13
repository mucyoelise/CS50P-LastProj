# ZodiacSign Project

#### Video Demo: .....................

#### Description: This project is designed to help users know their zodiac sign according to their inputed date of birth.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [License](#license)

## Introduction

Have you heard zodiac sign before? Well, in the concept of Astrology: a belief system that suggests a relationship between the positions and movements of celestial bodies--like planets, stars and moon--and events on the Earth, including human personalities, behaviors, and life events; zodiac is the part of astrology which believes that a person's personality depends on the position and movements of celestial bodies at the time of their birth. The zodiac is divided into 12 signs, each corresponding to specific dates in the calendar year. These signs are derived from the constellations the sun appears to pass through as the Earth orbits around it.

Want to know more about Astrology and Zodiac sign, click here: [Astrology/Zodiac_Docs](https://docs.google.com/document/d/1wB_t3Df-YiviWwG1Fy9tARbSY0cPbH1h/edit?usp=sharing&ouid=116133234786654777112&rtpof=true&sd=true).

## What Will Your Software Do?

This software aims to provide users with their zodiac sign according to the provided date of birth. Moreover, the users should choose if they want to get their personalities based on their zodiac sign as well as to receive them on their email. Note the user will be required to provide his/her gmail account for the sake of getting this information.

## How Will It Be Executed?

This software runs normally when executed, with the main logic defined under the main() function in the project.py script. Instead of passing parameters via the command line, the progam waits for user interaction during its runtime using Python input() function.

## Setup

### Libraries Used

This project utilizes several Python libraries to manage the application (in general) and send the user's zodiac sign and personalities through SMTP(Simple Mail Transfer Protocol) if requested by the user. 

The following libraries are used:

- **`datetime`**: Used to compute the range of zodiac signs' date with the user's provided date of birth.
- **`pyfiglet`**: Used to create ASCII art from the text(ZODIAC APP). To install this library, use (pip install pyfiglet).
- **`json`**: Used to read the json file contains personalities of different zodiac signs.
- **`re`**: Used to check user's entered email if it is valid.

- **`os`**: Used to interact with the operating system, so as to access on environment variables and working with file paths.
- **`dotenv`**: Used to load .env file so as to read credentials of the sender. To install this use (pip install python-dotenv).

- **`email.mime.text`**: Used to create email messages with text content.
- **`email.mime.multipart`**: Used to create multipart email message to be sent to the user--containing both plain text and attachments. 
- **`smtplib`**: Used to connect to an SMTP server and send email messages.

### Installation
Clone this repository to your local machine:

```markdown
git clone https://github.com/code50/191282522.git
cd Project
```

Libraries need to be installed before running:

- **`pyfiglet`**: To install this library, use (pip install pyfiglet).
- **`dotenv`**: To install this use (pip install python-dotenv).

### Usage

After completing the setup steps, you can run the project.py script to start interacting with the User Interface.

### Project Structure

The project structure is as follows:

```markdown
- Final Project/

  - project.py
  - personalities.json
  - .env
  - requirements.txt
  - test_project.py
  - gitignore
```

project.py: The main script that interacts with the user and displays all the information.

.env: file contains the APP password of the sender of email.

requirements.txt: List of required Python packages for the project.

test_project.py: Test file for testing the project functionalities.

.gitignore: File to exclude certain files from version control.

## Testing

To ensure the reliability of the project, testing has been implemented using the `pytest` framework. Test cases are defined in the `test_project.py` file. The testing script utilizes the **pytest** module so as to define and run test cases(Errors).

To run the tests, execute the following command:

```bash
pytest test_project.py
```

Note you will need to install this--if you don't have--before testing:

- **`pytest`**: install it using (pip install pytest).

### License

This project is licensed under the MIT License.