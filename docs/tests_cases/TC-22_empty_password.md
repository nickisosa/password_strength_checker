## TC-22 — Empty Password Input

**Labels:** `[EDGE CASE]` `[INPUT VALIDATION]` `[WEAK]`

**Purpose:**
Verify that the program handles an empty password input without crashing and correctly classifies the result as Weak.

**Test Input:**
No password was entered. The input field was left blank and submitted.

**Test Conditions:**

* Password length is below the minimum requirement.
* No uppercase characters are present.
* No lowercase characters are present.
* No numbers are present.
* No approved special characters are present.

**Expected Result:**

* Length check should fail.
* Uppercase check should fail.
* Lowercase check should fail.
* Number check should fail.
* Special-character check should fail.
* Character score should equal `0`.
* Password strength should be classified as `Weak`.
* The program should display improvement suggestions for all failed requirements.
* The program should continue running without an error.

**Actual Result:**
The program accepted the empty input and continued running without crashing. All password requirement checks failed as expected, the character score was calculated as `0`, and the password was classified as `Weak`. The program also displayed suggestions for each missing password requirement.

**Status:**
`PASS`

**Evidence:**
`test_cases/screenshots/TC-22_No_Input_Weak.md`

**Notes:**
This test confirmed that the program can handle empty user input safely and still complete the password evaluation process without producing an error.
