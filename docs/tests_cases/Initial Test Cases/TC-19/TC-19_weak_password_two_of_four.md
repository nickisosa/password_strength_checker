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

The initial test did not fully match the expected behavior and was recorded as `FAIL`.

**Status:**

`FAIL`

**Refactored:**

`YES`

**Retested:**

`YES`

**Retest Result:**

`PASS`

**Initial Evidence:**

`test_cases_Initial Test Cases/TC-19_weak_password_two_of_four_initial.png`

**Retest Evidence:**

`test_cases/Retest cases`

**Notes:**

This test verifies that the scoring logic does not classify a password as Medium or Strong when only two of the four character requirements are met.

**Refactoring Notes:**

The scoring logic was cleaned up by using Boolean results for each character requirement directly in `character_score`. This made the scoring process clearer and helped ensure that only successfully detected character requirements were counted.

**Retesting Notes:**

After refactoring, the password met the minimum length requirement and passed only the uppercase and lowercase checks. The numeric and approved special-character checks failed, producing a score of `2 out of 4`. The program correctly classified the password as `Weak` and displayed suggestions to add a number and an approved special character. The retest passed.
