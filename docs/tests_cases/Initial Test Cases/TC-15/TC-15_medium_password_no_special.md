## TC-15 — medium_password_no_special

**Labels:** `[SCORING]` `[MEDIUM]`

**Purpose:**

Verify that the program correctly classifies a password as Medium when it meets the minimum length requirement and passes exactly three out of the four character checks.

**Test Input:**

Password: `NoSpecialCharacters123`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

The password should pass the minimum length requirement and the uppercase, lowercase, and numeric checks. The special-character check should fail. The character score should equal `3`, and the final password strength should be classified as `Medium`.

**Actual Result:**

The password passed the minimum length requirement and the uppercase, lowercase, and numeric checks. No approved special character was detected. The character score was calculated as `3 out of 4`, and the password was correctly classified as `Medium`.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-15_medium_password_no_special_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that the scoring logic correctly assigns a Medium rating when the password meets the minimum length requirement and passes exactly three of the four character checks.

**Refactoring Notes:**

The special-character validation logic was cleaned up by storing the regex search result as a Boolean value using `has_special_char`. The Boolean result is then used directly in the character score, making the scoring logic easier to read and maintain.

**Retesting Notes:**

The test was repeated after refactoring. The password continued to pass the uppercase, lowercase, and numeric checks while failing the approved special-character check. The character score remained `3 out of 4`, and the password was correctly classified as `Medium`. The retest passed.
