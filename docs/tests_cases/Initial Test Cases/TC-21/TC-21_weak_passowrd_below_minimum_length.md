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
`[Fill in after testing]`

**Status:**
`PASS`

**Refactored:**
`NOT YET`

**Retested:**
`NOT YET`

**Retest Result:**
`[Fill in after retesting]`

**Initial Evidence:**
`test_cases/screenshots/TC-21_weak_password_minimum_length_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that meeting all four character requirements is not enough to receive a Strong rating if the password does not also meet the minimum length requirement. It confirms that the length requirement is enforced separately from the character score.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
