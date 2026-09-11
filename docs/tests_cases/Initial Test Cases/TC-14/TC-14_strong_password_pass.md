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
`screenshots/phase_3/TC-14_strong_password_pass_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that the scoring logic correctly assigns a Strong rating when the password meets the minimum length and passes all four character requirements.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
