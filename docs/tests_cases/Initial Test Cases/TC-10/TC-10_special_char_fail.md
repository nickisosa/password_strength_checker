## TC-10 — special_char_fail

**Labels:** `[SPECIAL]` `[REGEX]`

**Purpose:**
Verify that the program correctly detects when a password does not contain any approved special characters.

**Test Input:**
Password: `specialcharFail`

**Preconditions:**
Minimum password length is set to 8 characters.

Approved special characters are defined in the program's password policy.

**Expected Result:**
The special-character requirement should fail because the password does not contain any approved special characters. The program should display a message stating that no approved special character was detected and provide a suggestion to add at least one approved special character.

**Actual Result:**
The program correctly detected that no approved special characters were included. The special-character requirement failed as expected, and the program displayed the appropriate suggestion.

**Status:**
PASS

**Refactored:**
`YES`

**Retested:**
`YES`

**Retest Result:**
`PASS`

**Initial Evidence:**
`test_cases/Initial Test Cases/TC-10_special_char_fail_initial.png`

**Retest Evidence:**
`test_cases/Initial Test Cases/Restest Cases`

**Notes:**
`This test confirmed that the regex validation correctly identifies when a submitted password does not contain an approved special character.`

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`TC-10 Special characters expected to fail pass`
