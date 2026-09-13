## TC-16 — medium_password_no_number

**Labels:** `[SCORING]` `[MEDIUM]`

**Purpose:**

Verify that the program correctly classifies a password as Medium when it meets the minimum length requirement and passes exactly three out of the four character checks.

**Test Input:**

Password: `NoNumber$-Included`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

The password should pass the minimum length requirement and the uppercase, lowercase, and special-character checks. The numeric-character check should fail. The character score should equal `3`, and the final password strength should be classified as `Medium`.

**Actual Result:**

The password passed the minimum length requirement and the uppercase, lowercase, and approved special-character checks. No numeric character was detected. The character score was `3 out of 4`, and the password strength was correctly classified as `Medium`.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases/Initial Test Cases/TC-16_medium_password_no_number_initial.png`

**Retest Evidence:**

`test_cases/Initial Test Cases/Retest Cases`

**Notes:**

This test verifies that the scoring logic correctly assigns a Medium rating when the password meets the minimum length requirement and passes exactly three of the four character checks, even when the missing requirement is the numeric-character check.

**Refactoring Notes:**

The password validation logic was cleaned up by storing the numeric-character search result as a Boolean value and using the Boolean result directly in the character score. Variable names were also improved to make the code easier to read.

**Retesting Notes:**

The test was repeated after refactoring. The program produced the same expected result, confirming that the refactoring did not change the intended scoring behavior.

