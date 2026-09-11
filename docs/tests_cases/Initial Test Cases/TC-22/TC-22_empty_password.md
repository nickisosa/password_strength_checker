## TC-22 — empty_password_input

**Labels:** `[EDGE CASE]` `[INPUT VALIDATION]` `[WEAK]`

**Purpose:**
Verify that the program can handle an empty password input without crashing and correctly classify the result as Weak.

**Test Input:**
No password was entered. The input was left blank and submitted.

**Preconditions:**
Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

* Minimum length check should fail.
* Uppercase check should fail.
* Lowercase check should fail.
* Number check should fail.
* Special-character check should fail.
* Character score should equal `0`.
* Password strength should be classified as `Weak`.
* Improvement suggestions should be displayed for all failed requirements.
* The program should complete the evaluation without crashing or producing an error.

**Actual Result:**
The program accepted the empty input and completed the evaluation without crashing. All password requirement checks failed as expected. The character score was calculated as `0`, the password was classified as `Weak`, and improvement suggestions were displayed for each missing requirement.

**Status:**
`PASS`

**Refactored:**
`NOT YET`

**Retested:**
`NOT YET`

**Retest Result:**
`[Fill in after retesting]`

**Initial Evidence:**
`test_cases/screenshots/TC-22_empty_password_input_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test confirmed that the program can safely handle empty user input and still complete the password evaluation process correctly. It also verified that the program returns a character score of `0`, classifies the password as Weak, and provides suggestions for every missing requirement.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
