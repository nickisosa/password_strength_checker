## TC-12 — asterisk_special_character

**Labels:** `[SPECIAL]` `[REGEX]` `[EDGE CASE]`

**Purpose:**

Verify that the program correctly recognizes an asterisk (`*`) as an approved special character.

**Test Input:**

Password: `Aster*skPass*`

**Preconditions:**

Minimum password length is set to 8 characters.

The asterisk (`*`) is included in the approved special-character policy.

**Expected Result:**

The program should recognize the asterisk as an approved special character. The special-character requirement should pass, and the program should display a message confirming that an approved special character was detected.

**Actual Result:**

The program successfully recognized the asterisk as an approved special character and passed the special-character requirement.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-12_asterisk_char_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test confirms that the regex pattern correctly handles the asterisk as an approved special character rather than treating it only as a regex operator.

**Refactoring Notes:**

The special-character regex was cleaned up and stored in the `special_character_pattern` variable. The search result was converted into a Boolean value using `has_special_char`, which made the validation logic easier to read and use in the scoring process.

**Retesting Notes:**

The test was repeated after refactoring. The asterisk was still correctly recognized as an approved special character, and the special-character requirement passed as expected. The retest passed.
