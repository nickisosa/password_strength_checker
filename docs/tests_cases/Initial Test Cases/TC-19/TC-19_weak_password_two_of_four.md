## TC-19 — weak_password_two_of_four

**Labels:** `[SCORING]` `[WEAK]`

**Purpose:**
Verify that the program correctly classifies a password as Weak when it meets the minimum length requirement but only passes two out of the four character checks.

**Test Input:**
Password: `YuHgFFFdjssu`

**Preconditions:**
Minimum password length is set to 8 characters.

The program checks for:

* Uppercase characters
* Lowercase characters
* Numeric characters
* Approved special characters

**Expected Result:**
The password should meet the minimum length requirement but pass only two of the four character checks. The character score should equal `2`, and the final password strength should be classified as `Weak`.

The program should also display improvement suggestions for the two missing character requirements.

**Actual Result:**
`[Fill in after testing]`

**Status:**
`FAIL`

**Refactored:**
`NOT YET`

**Retested:**
`NOT YET`

**Retest Result:**
`[Fill in after retesting]`

**Initial Evidence:**
`screenshots/phase_3/TC-19_weak_password_two_of_four_initial.png`

**Retest Evidence:**
`[Add retest screenshot path later]`

**Notes:**
This test verifies that the scoring logic does not classify a password as Medium or Strong when only two of the four character requirements are met.

**Refactoring Notes:**
`[Document any code changes that affected this test later]`

**Retesting Notes:**
`[Document whether the result stayed the same after refactoring]`
