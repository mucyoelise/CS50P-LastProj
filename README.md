# ZodiacSign Project

#### Video Demo: .....................

#### Description: This project is designed to help users know their zodiac sign according to their inputed date of birth.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
  - [API Key](#api-key)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [License](#license)

## Introduction

This project utilizes the WeatherAPI to fetch weather and temperature information for a specified city. The project includes a command-line interface (CLI) that allows users to input the city name and choose between fetching the current weather or a forecast for a specific date.

## What Will Your Software Do?

This software aims to provide users with accurate weather and temperature information for a desired city. It can display both the current weather conditions and a forecast, helping users plan their activities accordingly. The project offers the following features:

- Retrieving and displaying current weather information (temperature, weather description, humidity, etc.).
- Retrieving and displaying a weather forecast for a specific date, including average temperature and humidity.
- Allowing users to choose between displaying temperature in Celsius or Fahrenheit using the `-i` flag.
- Allowing users to request a weather forecast for a specific date using the `-f` flag.
- Error handling for cases where the city name is invalid or the API key is incorrect.

## How Will It Be Executed?

The software is executed using the command-line interface (CLI) provided by the `project.py` script. Users will run the script followed by the desired city name and optional flags. For example:

    ``sh
    python project.py New York -i -f
    python project.py New York -if
    python project.py New York -i
    python project.py New York -f
    python project.py New York

## Setup

### Libraries Used

This project utilizes several Python libraries to manage the application (in general) and send the findings (Zodiac sign of the user) through SMTP when requested by the user. 
The following libraries are used:

- **`configparser`**: Used to read the API key from a configuration file.
- **`argparse`**: Used to parse command-line arguments provided by the user.
- **`sys`**: Provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
- **`requests`**: Used to make HTTP requests to the WeatherAPI and retrieve weather data.

### API Key

Before running the project, you'll need an API key from WeatherAPI. Follow these steps to get your API key:

1. Sign up on [WeatherAPI](https://www.weatherapi.com/signup.aspx) (if you haven't already).
2. Log in and navigate to your account settings.
3. Copy the generated API key.
4. Create a file named `secrets.ini` in the project directory and add your API key:

```ini
[openweather]
api_key=YOUR_API_KEY_HERE
```

### Installation

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/code50/105968684.git
   cd Final\ Project
   ```

2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

After completing the setup steps, you can use the project.py script to retrieve weather information for a specified city. Use the command-line arguments to customize the request:

python project.py <city>: Fetches current weather information for the given city.
python project.py <city> -i: Displays temperature in Fahrenheit.
python project.py <city> -f: Fetches weather forecast for the given city.
python project.py <city> -if: Displays temperature in Fahrenheit and fetches forecast.
python project.py <city> -i -f: Displays temperature in Fahrenheit and fetches forecast.

### Project Structure

The project structure is as follows:

```markdown
- Final Project/

  - project.py
  - secrets.ini
  - requirements.txt
  - test_project.py
  - gitignore
```

project.py: The main script that interacts with the WeatherAPI and displays weather information.
secrets.ini: Configuration file containing the WeatherAPI API key.
requirements.txt: List of required Python packages for the project.
test_project.py: Test file for testing the project functionalities.
.gitignore: File to exclude certain files from version control.

## Testing

To ensure the reliability of the project, testing has been implemented using the `pytest` framework. Test cases are defined in the `test_project.py` file. The testing script utilizes the following libraries:

- **`unittest.mock`**: Used for mocking external interactions, such as API calls, during testing.
- **`pytest`**: Used as the testing framework to define and run test cases.

To run the tests, execute the following command:

```bash
pytest test_project.py
```

### License

This project is licensed under the MIT License.
