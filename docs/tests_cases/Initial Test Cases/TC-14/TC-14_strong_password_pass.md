## TC-14 — strong_password

**Labels:** `[SCORING]` `[STRONG]`

**Purpose:**

Verify that the program correctly classifies a password as Strong when it meets the minimum length requirement and passes all four character checks.

**Test Input:**

Password: `All-4Character$Work`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

The password should pass the minimum length requirement and all four character checks. The character score should equal `4`, and the final password strength should be classified as `Strong`.

**Actual Result:**

The password passed the minimum length requirement and successfully passed the uppercase, lowercase, numeric, and approved special-character checks. The character score was calculated as `4 out of 4`, and the password was correctly classified as `Strong`.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-14_strong_password_pass_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that the scoring logic correctly assigns a Strong rating when the password meets the minimum length requirement and passes all four character requirements.

**Refactoring Notes:**

The validation logic was cleaned up by storing each character check as a Boolean value and using those Boolean results directly in `character_score`. This made the scoring logic easier to read while keeping the Strong password requirements unchanged.

**Retesting Notes:**

The test was repeated after refactoring. The password continued to meet the minimum length requirement and passed all four character checks. The character score remained `4 out of 4`, and the password was correctly classified as `Strong`. The retest passed.

