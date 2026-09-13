## TC-17 — medium_password_no_uppercase

**Labels:** `[SCORING]` `[MEDIUM]`

**Purpose:**

Verify that the program correctly classifies a password as Medium when it meets the minimum length requirement and passes exactly three out of the four character checks.

**Test Input:**

Password: `no_uppercase12$`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

The password should pass the minimum length requirement and the lowercase, numeric, and special-character checks. The uppercase check should fail. The character score should equal `3`, and the final password strength should be classified as `Medium`.

**Actual Result:**

The password passed the minimum length requirement and the lowercase, numeric, and approved special-character checks. No uppercase character was detected. The character score was `3 out of 4`, and the password strength was correctly classified as `Medium`.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-17_medium_password_no_uppercase_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that the scoring logic correctly assigns a Medium rating when the password meets the minimum length requirement and passes exactly three of the four character checks, even when the missing requirement is uppercase.

**Refactoring Notes:**

The uppercase validation logic was cleaned up by storing the regex search result as a Boolean value using `has_uppercase`. The Boolean result is then used directly in the character score, making the code easier to read and maintain.

**Retesting Notes:**

The test was repeated after refactoring. The program produced the same expected result, confirming that the refactoring did not change the intended scoring behavior.

