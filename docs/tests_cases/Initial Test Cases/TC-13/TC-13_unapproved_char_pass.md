## TC-13 — unapproved_special_character

**Labels:** `[SPECIAL]` `[REGEX]` `[POLICY]`

**Purpose:**
Verify that the program does not count a special character as valid when that character is not included in the approved special-character policy.

**Test Input:**
Password: `sgdhhdjUHV))`

**Preconditions:**
Minimum password length is set to 8 characters.

The program only recognizes the following approved special characters:

`! @ # $ % & _ - * +`

**Expected Result:**
The unapproved symbol should not satisfy the special-character requirement. The program should report that no approved special character was detected and provide a suggestion to add an approved special character.

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
`screenshots/phase_2/TC-13_unapproved_char_pass_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that the special-character validation follows the defined password policy and does not automatically accept every symbol as an approved character.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
