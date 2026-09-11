## TC-09 — special_char_pass

**Labels:** `[SPECIAL]` `[REGEX]`

**Purpose:**
Verify that the program correctly detects when a password contains at least one approved special character.

**Test Input:**
Password: `$pecialCharPass13`

**Preconditions:**
Minimum password length is set to 8 characters.

Approved special characters are defined in the program's password policy.

**Expected Result:**
The special-character requirement should pass because the password contains at least one approved special character. The program should display a message confirming that an approved special character was detected.

**Actual Result:**
The program correctly detected the approved special character and confirmed that the special-character requirement was met.

**Status:**
PASS

**Refactored:**
`NOT YET`

**Retested:**
`NOT YET`

**Retest Result:**
`[Fill in after retesting]`

**Initial Evidence:**
`screenshots/phase_2/TC-09_special_char_pass_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test confirmed that the regex validation correctly recognizes approved special characters in the submitted password.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
