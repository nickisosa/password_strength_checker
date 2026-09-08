#This project was created to check the strength of a password
import re
print("+--------------------------------------+")
print("|       PASSWORD STRENGTH CHECKER      |")
print("+--------------------------------------+")
#General Variables
create_password = input("Create a new password: ")
print("_" * 65)
min_length = 8
passed = True
failed = False
special_characters = r"[!@#$%&_\-*+]"



#Length Checker
if len(create_password) >= min_length:
# Temporary result variables used to verify each length check during testing
    length_check = passed
    print("-Minimum length requirement met.")
else:
    length_check = failed
    print("-Minimum length requirement not met.")
    print("Suggestion: Use a password with atleast 8 characters.")
print("*" * 65)
#Uppercase Condition
upcase_result = re.search(r"[A-Z]", create_password)

if upcase_result:
    # Temporary result variables used to verify each Upper check during testing
    upcase_result = passed
    print("-Uppercase character detected.")
else:
    upcase_result = failed
    print("-No uppercase character detected.")
    print("Suggestion: Add atleast one uppercase letter.")
print("=" * 50)
#Lowercase Condition
lowcase_result = re.search(r"[a-z]", create_password)

if lowcase_result:
    # Temporary result variables used to verify each Lowercase check during testing
    lowcase_result = passed
    print("-Lowercase character detected!")
else:
    lowcase_result = failed
    print("-No lowercase character detected!")
    print("Suggestion: Add atleast one lowercase letter.")
print("=" * 50)
#Numbercase Condition
numcase_result = re.search(r"[0-9]", create_password)

if numcase_result:
    # Temporary result variables used to verify each Numbercase check during testing
    numcase_result = passed
    print("-Numeric character detected.!")
else:
    numcase_result = failed
    print("-No numeric characters detected.")
    print("Suggestion: Add atleast one number.")
print("=" * 50)
#Special Characters Condition
special_result = re.search(special_characters, create_password)

if special_result:
    # Temporary result variables used to verify special character check during testing
    special_result = passed
    print("-Approved special character detected.")
else:
    special_result = failed
    print("-No approved special character detected.")
    print("Suggestion: Add atleast one approved special character(s).")
print("*" * 65)

#Strength Checker - Weak, Medium, or Strong

character_score = sum([upcase_result, lowcase_result, numcase_result, special_result])

if len(create_password) >= min_length and character_score == 4:
    strength = "Strong"
elif len(create_password) >= min_length and character_score == 3:
    strength = "Medium"
else:
    strength = "Weak"
print("Character Requirement Met:", character_score, "out of 4")
print("Password Strength:", strength)
    