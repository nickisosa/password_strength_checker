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
`test_cases/screenshots/TC-23_password_with_spaces_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test helps confirm that spaces are handled consistently with the current password policy. It also checks that the presence of a space does not accidentally satisfy the approved special-character requirement.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
