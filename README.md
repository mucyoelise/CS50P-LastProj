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

Have you heard zodiac sign before? Well, in the concept of Astrology: a belief system that suggests a relationship between the positions and movements of celestial bodies--like planets, stars and moon--and events on the Earth, including human personalities, behaviors, and life events; zodiac is the part of astrology which believes that a person's personality depends on the position and movements of celestial bodies at the time of their birth. The zodiac is divided into 12 signs, each corresponding to specific dates in the calendar year. These signs are derived from the constellations the sun appears to pass through as the Earth orbits around it.

Want to know more about Astrology [click here](https://docs.google.com/document/d/1wB_t3Df-YiviWwG1Fy9tARbSY0cPbH1h/edit?usp=sharing&ouid=116133234786654777112&rtpof=true&sd=true).

## What Will Your Software Do?

This software aims to provide users with their zodiac sign according to provided date of birth. Moreover, the users should choose if they want to get their personalities based on their zodiac sign as well as to receive them on their emails. Note the user will be required to provide his/her gmail account for the sake of getting this information on his/her email.

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

This project utilizes several Python libraries to manage the application (in 