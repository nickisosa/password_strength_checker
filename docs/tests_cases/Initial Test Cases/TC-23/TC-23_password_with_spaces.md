## TC-23 — password_with_spaces

**Labels:** `[EDGE CASE]` `[INPUT VALIDATION]` `[POLICY]`

**Purpose:**

Verify how the program handles a password that contains one or more spaces and confirm whether the behavior matches the current password policy.

**Test Input:**

Password: `with spaces 123$`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

Spaces are not currently listed as approved special characters.

**Expected Result:**

The program should count the space as part of the password length but should not count it as an approved special character. The final strength rating should depend only on the requirements that are actually met.

**Actual Result:**

The password met the minimum length requirement. The lowercase, numeric, and approved special-character checks passed, while the uppercase check failed. The spaces were accepted as part of the password input and contributed to the total password length but were not treated as approved special characters. The character score was `3 out of 4`, and the password was correctly classified as `Medium`.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-23_password_with_spaces_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test confirms that spaces are handled consistently with the current password policy. Spaces can exist within the password and count toward its total length, but they do not satisfy the approved special-character requirement. The password strength is determined only by the requirements that are actually met.

**Refactoring Notes:**

The special-character validation continued to use the defined regex pattern containing only approved special characters. The validation results were stored as Boolean values and used directly in the scoring logic, helping ensure that spaces were not accidentally treated as approved special characters.

**Retesting Notes:**

The test was repeated after refactoring. The program continued to accept spaces as part of the password length without treating them as approved special characters. The password passed the lowercase, numeric, and approved special-character checks, failed the uppercase check, received a score of `3 out of 4`, and was correctly classified as `Medium`. The retest passed.
