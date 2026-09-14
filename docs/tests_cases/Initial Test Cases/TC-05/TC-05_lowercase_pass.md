## TC-05 — lowercase_pass

**Labels:** `[LOWERCASE]`

**Purpose:**
Verify that the program correctly detects when a password contains at least one lowercase character.

**Test Input:**
Password: `[Enter your test password here]`

**Preconditions:**
Minimum password length is set to 8 characters.

**Expected Result:**
The lowercase requirement should pass because the password contains at least one lowercase letter. The program should display a message confirming that a lowercase character was detected.

**Actual Result:**
The program correctly detected the lowercase character and confirmed that the lowercase requirement was met.

**Status:**
`PASS`

**Refactored:**
`YES`

**Retested:**
`YES`

**Retest Result:**
`PASS`

**Initial Evidence:**
`test_cases/Initial Test Cases/TC-05_Lowercase_Pass_Initial.png`
`test_cases/Initial Test Cases/Retest Cases`

**Notes:**
This test confirmed that the lowercase validation correctly recognizes lowercase letters in the submitted password.

**Refactoring Notes:**
`When refactoring, I removed unneccary code and clutter`

**Retesting Notes:**
`Retesting TC-05 passed and lowercase detection recognized.`
