## TC-24 — very_long_password

**Labels:** `[EDGE CASE]` `[LENGTH]` `[SCORING]`

**Purpose:**
Verify that the program can process a very long password without crashing or producing incorrect results.

**Test Input:**
Password: `VeryLONGPassword@-IntialPassword33$*-SuperLONGpassword-ExtremelyLONG`

**Preconditions:**
Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

The program currently enforces a minimum password length but does not enforce a maximum length.

**Expected Result:**
The program should accept the long password and complete all validation checks without producing an error. If all four character requirements are present, the character score should equal `4`, and the password should be classified as `Strong`.

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
`test_cases/screenshots/TC-24_very_long_password_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that the program can handle a password that is significantly longer than the minimum requirement without affecting the validation or scoring logic.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
