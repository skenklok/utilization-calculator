# Utilization Calculator

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Leap Year Support](#leap-year-support)
6. [Validation and Error Handling](#validation-and-error-handling)
7. [Packaging the App](#packaging-the-app)
8. [Contributing](#contributing)
9. [License](#license)

## Overview

Utilization Calculator is a desktop application that assists professionals and businesses in calculating the number of additional billable days needed to reach their target utilization rate. The application is built using Python's Tkinter library and offers an easy-to-use interface.

## Features

- **Current Utilization Input**: Input your current billable utilization rate as a percentage.
- **Target Utilization Input**: Specify the desired billable utilization rate you want to achieve by the end of the year.
- **Date Input**: Enter the current date to consider the remaining workdays in the year for calculations.
- **Leap Year Support**: Automatically adjusts calculations for leap years.
- **Validation & Error Handling**: Comprehensive input validation and user-friendly error messages.

## Installation

### Requirements

- Python 3.x
- Tkinter

### Steps

1. Clone this repository to your local machine.
    ```
    git clone https://github.com/your-username/utilization-calculator.git
    ```
2. Navigate to the cloned directory.
    ```
    cd utilization-calculator
    ```
3. Run `app.py` to start the application.
    ```
    python3 app.py
    ```

## Usage

1. Open the application.
2. You will see input fields for "Current Utilization (%)", "Target Utilization (%)", and "Current Date (YYYY-MM-DD)".
3. Fill in these fields with the appropriate values.
4. Click the "Calculate" button.
5. The application will display the number of additional billable days needed to meet your target utilization rate and the number of workdays remaining in the current year.

## Leap Year Support

The application automatically detects if the current year is a leap year and adjusts the total number of workdays in the year accordingly. If it is a leap year, a notification will be displayed.

## Validation and Error Handling

The application ensures that all input fields are correctly filled out. If an input is missing or incorrect, an error message will be displayed, guiding the user to correct the input.

## Packaging the App

To convert this Python application into a standalone executable for macOS, you can use packaging tools like PyInstaller or cx_Freeze. This will allow users to run the app by simply double-clicking an icon.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE.md` for more details.

---

Feel free to customize this README as you see fit for your project!