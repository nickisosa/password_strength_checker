## TC-21 — weak_password_below_minimum_length

**Labels:** `[SCORING]` `[WEAK]` `[EDGE CASE]` `[LENGTH]`

**Purpose:**

Verify that the program correctly classifies a password as Weak when it contains all four character requirements but does not meet the minimum length requirement.

**Test Input:**

Password: `uNder8$`

**Preconditions:**

Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**

* Minimum length check should fail.
* Uppercase check should pass.
* Lowercase check should pass.
* Number check should pass.
* Special-character check should pass.
* Character score should equal `4`.
* Password strength should still be classified as `Weak` because the minimum length requirement was not met.
* The program should display a suggestion to increase the password length.

**Actual Result:**

The password failed the minimum length requirement but successfully passed the uppercase, lowercase, numeric, and approved special-character checks. The character score was calculated as `4 out of 4`. Because the password did not meet the minimum length requirement, the program correctly classified it as `Weak` and displayed a suggestion to use a password with at least 8 characters.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-21_weak_password_minimum_length_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that meeting all four character requirements is not enough to receive a Strong rating if the password does not also meet the minimum length requirement. It confirms that the length requirement is enforced separately from the character score.

**Refactoring Notes:**

The length check remained separate from the four character requirements, while the character validation results were stored as Boolean values and used directly in `character_score`. This kept the password length requirement independent from the character score and made the final strength logic easier to understand.

**Retesting Notes:**

The test was repeated after refactoring. The password still received a character score of `4 out of 4`, but because it was shorter than the required minimum length, the program correctly classified it as `Weak`. The expected length suggestion was also displayed, confirming that the refactoring did not change the intended behavior.
