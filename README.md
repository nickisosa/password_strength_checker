# Password Strength Checker

## Overview

The Password Strength Checker is a Python command-line application designed to evaluate a user-submitted password against basic password-security requirements.

The application examines password length and several character requirements before assigning the password a strength rating of **Weak**, **Medium**, or **Strong**.

This project was created as a cybersecurity training project to practice Python programming, data validation, regular expressions, security-policy implementation, testing, troubleshooting, and technical documentation.

## Problem / Security Need

Weak passwords can increase the risk of unauthorized account access and credential-based attacks.

Organizations commonly establish password policies that define minimum requirements for password length and character composition. This project demonstrates how those requirements can be translated into programmatic validation checks.

## Project Objectives

The objectives of this project are to:

* Accept a password entered by a user.
* Validate the password against a minimum-length requirement.
* Detect uppercase characters.
* Detect lowercase characters.
* Detect numerical characters.
* Detect approved special characters.
* Track how many character requirements are satisfied.
* Classify the password as Weak, Medium, or Strong.
* Provide a foundation for password-improvement recommendations.
* Practice testing and technical documentation.

## Features

The current application includes:

* User password input
* Minimum-length validation
* Uppercase-character detection
* Lowercase-character detection
* Number detection
* Special-character detection
* Regex-based character validation
* Boolean validation results
* Character-requirement scoring
* Weak, Medium, and Strong classification
* Console output for testing and verification

## Security Criteria / Policy Summary

The password checker evaluates five primary security criteria:

1. Minimum password length
2. Uppercase character
3. Lowercase character
4. Numerical character
5. Approved special character

The four character-based requirements are converted into a character score.

### Strong

A Strong password:

* Meets the minimum length requirement
* Passes all 4 character checks

### Medium

A Medium password:

* Meets the minimum length requirement
* Passes 3 out of 4 character checks

### Weak

A password is classified as Weak when it does not meet the requirements for either Medium or Strong.

The current minimum password length is **8 characters**.

## Technologies Used

* Python
* Python `re` module
* Regular expressions
* Command-line interface
* Git / GitHub for version control and project documentation

## How to Run

1. Make sure Python is installed.
2. Download or clone the repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python password_checker.py
```

5. Enter a test password when prompted.
6. Review the validation and strength results displayed in the console.

Do not use real account passwords when testing the application.

## Testing

The application is manually tested using passwords designed to trigger different combinations of security requirements.

Testing includes:

* Passwords meeting all requirements
* Passwords meeting 3 out of 4 character requirements
* Passwords meeting fewer than 3 character requirements
* Passwords below the minimum length
* Passwords without uppercase letters
* Passwords without lowercase letters
* Passwords without numbers
* Passwords without special characters
* Empty input

Detailed testing documentation is located in the `test_cases` directory.

## Security Considerations

This project is intended for cybersecurity education and demonstrates basic password-policy validation.

The application evaluates password composition but does not determine whether a password has previously appeared in a data breach or whether it is resistant to every type of password attack.

Passwords entered into the application should be test passwords only. Real passwords should not be stored in the source code, screenshots, repository, or testing documentation.

## Project Structure

```text
password_strength_checker/
│
├── password_checker.py
├── README.md
│
├── test_cases/
│   ├── test_cases.md
│   └── screenshots/
│
└── docs/
    └── Password_Strength_Checker_Project_Instructions.pdf
```

## Lessons Learned

This project provided practice with:

* Translating a security policy into program logic
* Python conditional statements
* Boolean values
* Regular expressions
* `re.search()`
* String-length validation
* Combining individual validation results into a score
* Debugging unexpected program behavior
* Distinguishing regex Match objects from Boolean results
* Manual software testing
* Writing technical project documentation

Additional lessons will be documented as the project is completed.

## Future Improvements

Planned improvements include:

* Providing password-specific improvement suggestions
* Improving the readability of console output
* Refactoring temporary testing code after validation is complete
* Adding stronger input handling
* Expanding test coverage
* Exploring automated unit testing
* Refactoring the application with functions
* Potentially creating an object-oriented version using a Python class
