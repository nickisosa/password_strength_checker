## TC-20 — weak_password_one_of_four

**Labels:** `[SCORING]` `[WEAK]` `[SUGGESTIONS]`

**Purpose:**

Verify that the program correctly classifies a password as Weak when only one of the four character requirements is met and that improvement suggestions are provided for each failed requirement.

**Test Input:**

Password: `yetr`

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
* Lowercase check should pass.
* Number check should fail.
* Special-character check should fail.
* Character score should equal `1`.
* Password strength should be classified as `Weak`.
* The program should display suggestions for the failed length, uppercase, number, and special-character requirements.

**Actual Result:**

The program correctly identified that the password did not meet the minimum length requirement and did not contain uppercase letters, numbers, or approved special characters. The lowercase requirement passed successfully. The character score was calculated as `1`, and the final password strength was classified as `Weak`. The program also displayed a separate improvement suggestion for each failed requirement.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-20_Weak_Password_1_Char.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test confirmed that the program can handle multiple failed password requirements at the same time. It correctly recognized that lowercase was the only character requirement met while identifying the missing uppercase, number, and special-character requirements. The program also provided multiple improvement suggestions instead of stopping after the first failed check.

**Refactoring Notes:**

The validation and scoring logic were cleaned up by storing each character check as a Boolean result and using those Boolean values directly in `character_score`. This made the logic easier to follow while keeping the individual suggestions for failed requirements.

**Retesting Notes:**

The test was repeated after refactoring. The password still failed the minimum length, uppercase, numeric, and approved special-character requirements while passing the lowercase check. The character score remained `1 out of 4`, the password was correctly classified as `Weak`, and all expected improvement suggestions were displayed. The retest passed.
