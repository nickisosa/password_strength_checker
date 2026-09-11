## TC-12 — asterisk_special_character

**Labels:** `[SPECIAL]` `[REGEX]` `[EDGE CASE]`

**Purpose:**
Verify that the program correctly recognizes an asterisk (`*`) as an approved special character.

**Test Input:**
Password: `Aster*skPass* `

**Preconditions:**
Minimum password length is set to 8 characters.

The asterisk (`*`) is included in the approved special-character policy.

**Expected Result:**
The program should recognize the asterisk as an approved special character. The special-character requirement should pass, and the program should display a message confirming that an approved special character was detected.

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
`screenshots/phase_2/TC-12_asterisk_char_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test confirms that the regex pattern correctly handles the asterisk as an approved special character rather than treating it only as a regex operator.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
