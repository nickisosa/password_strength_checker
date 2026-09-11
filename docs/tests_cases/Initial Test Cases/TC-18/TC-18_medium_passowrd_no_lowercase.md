## TC-18 — medium_password_no_lowercase

**Labels:** `[SCORING]` `[MEDIUM]`

**Purpose:**
Verify that the program correctly classifies a password as Medium when it meets the minimum length requirement and passes exactly three out of the four character checks.

**Test Input:**
Password: `NO_LOWERCASE123$`

**Preconditions:**
Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**
The password should pass the minimum length requirement and the uppercase, numeric, and special-character checks. The lowercase check should fail. The character score should equal `3`, and the final password strength should be classified as `Medium`.

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
`screenshots/phase_3/TC-18_medium_password_no_lowercase_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that the scoring logic correctly assigns a Medium rating when the password meets the minimum length requirement and passes exactly three of the four character checks, even when the missing requirement is lowercase.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
