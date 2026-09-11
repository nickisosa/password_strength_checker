## TC-04 — upcase_fail

**Labels:** `[UPPERCASE]`

**Purpose:**
Verify that the program correctly detects when a password does not contain an uppercase character.

**Test Input:**
Password: `hdhjkwidk`

**Preconditions:**
Minimum password length is set to 8 characters.

**Expected Result:**
The uppercase requirement should fail because the password does not contain any uppercase letters. The program should display a message stating that no uppercase character was detected and provide a suggestion to add at least one uppercase letter.

**Actual Result:**
The program correctly detected that no uppercase character was included. The uppercase requirement failed as expected, and the program displayed the appropriate suggestion.

**Status:**
PASS

**Refactored:**
YES

**Retested:**
YES / NO

**Evidence:**
`screenshots/phase_2/TC-04_Uppercase_Fail_Initial.png`
`Screenshots/phase_4/???`

**Notes:**

