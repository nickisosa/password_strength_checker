## List of test cases:
| Test ID   | Label                  | Test Purpose                                                     | Expected Result                                                    |
| --------- | ---------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
|✅  **TC-01** | `[LENGTH]`             | Password is exactly 8 characters                                 | Length check passes                                                |
|✅  **TC-02** | `[LENGTH]`             | Password is fewer than 8 characters                              | Length check fails                                                 |
|✅ **TC-03** | `[UPPERCASE]`          | Password contains at least one uppercase letter                  | Uppercase check passes                                             |
|✅**TC-04** | `[UPPERCASE]`          | Password contains no uppercase letters                           | Uppercase check fails                                              |
|✅ **TC-05** | `[LOWERCASE]`          | Password contains at least one lowercase letter                  | Lowercase check passes                                             |
|✅ **TC-06** | `[LOWERCASE]`          | Password contains no lowercase letters                           | Lowercase check fails                                              |
|✅ **TC-07** | `[NUMBER]`             | Password contains at least one number                            | Number check passes                                                |
|✅ **TC-08** | `[NUMBER]`             | Password contains no numbers                                     | Number check fails                                                 |
|✅ **TC-09** | `[SPECIAL] [REGEX]`    | Password contains an approved special character                  | Special-character check passes                                     |
|✅ **TC-10** | `[SPECIAL] [REGEX]`    | Password contains no approved special character                  | Special-character check fails                                      |
|✅ **TC-11** | `[SPECIAL] [REGEX]`    | Password contains a hyphen `-`                                   | Hyphen is correctly recognized                                     |
|✅ **TC-12** | `[SPECIAL] [REGEX]`    | Password contains `*` or another regex-sensitive approved symbol | Symbol is correctly recognized                                     |
|✅ **TC-13** | `[SPECIAL] [POLICY]`   | Password contains a symbol that is **not** in your approved list | Special-character requirement fails                                |
|✅ **TC-14** | `[SCORING] [STRONG]`   | Valid length + all 4 character categories                        | Character score = 4; Strength = Strong                             |
|✅ **TC-15** | `[SCORING] [MEDIUM]`   | Valid length + 3/4, missing special character                    | Character score = 3; Strength = Medium                             |
|✅ **TC-16** | `[SCORING] [MEDIUM]`   | Valid length + 3/4, missing number                               | Character score = 3; Strength = Medium                             |
|✅ **TC-17** | `[SCORING] [MEDIUM]`   | Valid length + 3/4, missing uppercase                            | Character score = 3; Strength = Medium                             |
|✅ **TC-18** | `[SCORING] [MEDIUM]`   | Valid length + 3/4, missing lowercase                            | Character score = 3; Strength = Medium                             |
|✅ **TC-19** | `[SCORING] [WEAK]`     | Valid length + only 2/4 character categories                     | Character score = 2; Strength = Weak                               |
|✅  **TC-20** | `[SCORING] [WEAK]`     | Valid length + only 1/4 character categories                     | Character score = 1; Strength = Weak                               |
|✅ **TC-21** | `[EDGE CASE] [LENGTH]` | Under 8 characters but contains all 4 character categories       | Strength = Weak                                                    |
|✅  **TC-22** | `[EDGE CASE]`         | Empty password input                                             | Strength = Weak; program should not crash                           |
|✅ **TC-23** | `[EDGE CASE]`          | Password contains spaces                                         | Record actual behavior and decide whether this matches your policy |
|✅ **TC-24** | `[EDGE CASE]`          | Very long password containing all requirements                   | Program should still process it correctly                          |
