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

The program correctly identified that the password did not contain an approved special character. The unapproved `)` symbols did not satisfy the special-character requirement, and the program displayed a suggestion to add an approved special character.

**Status:**

`PASS`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-13_unapproved_char_pass_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that the special-character validation follows the defined password policy and does not automatically accept every symbol as an approved character.

**Refactoring Notes:**

The special-character validation was cleaned up by using the `special_character_pattern` regex and storing the result as a Boolean value. This helped make the approved-character policy clearer and ensured that only the symbols included in the regex pattern were accepted.

**Retesting Notes:**

The test was repeated after refactoring. The `)` symbols were still correctly rejected as unapproved special characters, and the program continued to display the appropriate suggestion. The retest passed.

