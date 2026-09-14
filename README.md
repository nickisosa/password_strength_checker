# Password Strength Checker

## Overview

The Password Strength Checker is a Python command-line application designed to evaluate a user-submitted password against basic password-security requirements.

The application examines password length and several character requirements before assigning the password a strength rating of **Weak**, **Medium**, or **Strong**.

This project was created as a cybersecurity training project to practice Python programming, data validation, regular expressions, security-policy implementation, testing, troubleshooting, refactoring, and technical documentation.

## Problem / Security Need

Weak passwords can increase the risk of unauthorized account access and credential-based attacks.

Organizations commonly establish password policies that define minimum requirements for password length and character composition. This project demonstrates how those requirements can be translated into programmatic validation checks.

The application also provides suggestions when password requirements are not met, helping the user understand how the password could be improved.

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
* Provide improvement suggestions for failed requirements.
* Practice manual software testing and retesting.
* Practice troubleshooting and code refactoring.
* Create professional technical documentation.

## Features

The completed application includes:

* User password input
* Minimum-length validation
* Uppercase-character detection
* Lowercase-character detection
* Number detection
* Approved special-character detection
* Regex-based character validation
* Boolean validation results
* Character-requirement scoring
* Weak, Medium, and Strong classification
* Password-specific improvement suggestions
* Organized console output
* Edge-case handling
* Manual test-case validation
* Post-refactoring retesting

## Security Criteria / Policy Summary

The password checker evaluates five primary security criteria:

1. Minimum password length
2. Uppercase character
3. Lowercase character
4. Numerical character
5. Approved special character

The current minimum password length is **8 characters**.

The approved special characters are:

`! @ # $ % & _ - * +`

The four character-based requirements are converted into a character score ranging from `0` to `4`.

### Strong

A Strong password:

* Meets the minimum length requirement
* Passes all 4 character checks

### Medium

A Medium password:

* Meets the minimum length requirement
* Passes exactly 3 out of 4 character checks

### Weak

A password is classified as Weak when it does not meet the requirements for either Medium or Strong.

A password can receive a character score of `4 out of 4` and still be classified as Weak if it does not meet the minimum length requirement.

## Technologies Used

* Python
* Python `re` module
* Regular expressions
* Boolean logic
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
6. Review the validation checks, suggestions, character score, and password-strength result displayed in the console.

Do not use real account passwords when testing the application.

## Testing

The application was manually tested using **24 documented test cases** designed to verify individual validation checks, scoring behavior, password classifications, special-character handling, and edge cases.

Testing included:

* Passwords meeting all requirements
* Passwords meeting 3 out of 4 character requirements
* Passwords meeting fewer than 3 character requirements
* Passwords below the minimum length
* Passwords without uppercase letters
* Passwords without lowercase letters
* Passwords without numbers
* Passwords without approved special characters
* Approved special-character testing
* Unapproved special-character testing
* Hyphen regex testing
* Asterisk regex testing
* Empty password input
* Passwords containing spaces
* Very long passwords
* Password improvement suggestions
* Strong, Medium, and Weak scoring behavior

After the code was refactored, the documented test cases were repeated to confirm that the cleanup did not change the intended behavior of the application.

Initial and retest evidence is included with the project testing documentation.

## Security Considerations

This project is intended for cybersecurity education and demonstrates basic password-policy validation.

The application evaluates password composition but does not determine whether a password has previously appeared in a data breach or whether it is resistant to every type of password attack.

Passwords entered into the application should be test passwords only. Real passwords should not be stored in the source code, screenshots, repository, or testing documentation.

The project also demonstrates that password composition rules are only one part of password security. A password meeting the application's Strong requirements should not automatically be considered secure in every real-world situation.

## Project Structure

```text
password_strength_checker/

├── password_checker.py
├── README.md
│
├── test_cases/
│   ├── test_cases.md
│   └── Retest cases/
│
├── test_cases_Initial Test Cases/
│
└── docs/
    ├── Password_Strength_Checker_Project_Instructions.pdf
    └── Password_Strength_Checker_Final_Technical_Report.pdf
```

## Lessons Learned

This project provided hands-on practice with:

* Translating a security policy into program logic
* Python conditional statements
* Boolean values
* Regular expressions
* `re.search()`
* Regex character classes
* String-length validation
* Combining validation results into a character score
* Creating Weak, Medium, and Strong classification logic
* Providing suggestions based on failed requirements
* Debugging unexpected program behavior
* Distinguishing regex Match objects from Boolean values
* Handling special characters inside regex patterns
* Testing edge cases
* Creating structured manual test cases
* Retesting after code changes
* Refactoring code without changing its intended behavior
* Improving variable names and code readability
* Writing technical project documentation

One of the most important lessons from this project was understanding that working code is only one part of development. Testing, troubleshooting, documentation, and refactoring are also important parts of creating a complete project.

## Future Improvements

Possible future improvements include:

* Refactoring the application into reusable functions
* Creating an object-oriented version using a Python class
* Adding automated unit testing
* Hiding password input while the user types
* Adding stronger or customizable password-policy requirements
* Checking passwords against common-password lists
* Adding breached-password detection through an appropriate security service or API
* Adding additional password-strength factors beyond character composition
* Creating a graphical user interface
* Expanding automated error and input handling

