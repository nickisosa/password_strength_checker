## TC-11 — hyphen_special_character

**Labels:** `[SPECIAL]` `[REGEX]` `[EDGE CASE]`

**Purpose:**

Verify that the program correctly recognizes a hyphen (`-`) as an approved special character.

**Test Input:**

Password: `approved-hyphen`

**Preconditions:**

Minimum password length is set to 8 characters.

The hyphen (`-`) is included in the approved special-character policy.

**Expected Result:**

The program should recognize the hyphen as an approved special character. The special-character requirement should pass, and the program should display a message confirming that an approved special character was detected.

**Actual Result:**

The program successfully recognized the hyphen as an approved special character. The special-character requirement passed, and the program correctly displayed a message confirming that an approved special character was detected.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-11_Hyphen_Special_Character_Initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test specifically checks that the hyphen is handled correctly by the regex pattern and is not mistakenly interpreted only as part of a character range.

**Refactoring Notes:**

Unnecessary code and old comments were removed during cleanup. The special-character regex was also stored in the `special_character_pattern` variable, and the search result was converted into a Boolean value using `has_special_char`.

**Retesting Notes:**

The test was repeated after refactoring. The hyphen was still correctly recognized as an approved special character, and the special-character requirement passed as expected. The retest passed.

