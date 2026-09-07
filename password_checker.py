#This project was created to check the strength of a password
import re

#General Variables
create_password = input("Create a new password: ")
min_length = 8
passed = True
failed = False
special_characters = r"[!@#$%&_\-*+]"



#Length Checker
if len(create_password) >= min_length:
# Temporary result variables used to verify each length check during testing
    length_check = passed
    print("Length Check Reached")
else:
    length_check = failed
    print("Length Check Not Reached")

#Uppercase Condition
upcase_result = re.search(r"[A-Z]", create_password)

if upcase_result:
    # Temporary result variables used to verify each Upper check during testing
    upcase_result = passed
    print("Atleast one Character is Uppercase!")
else:
    upcase_result = failed
    print("No Characters Are Uppercase")

#Lowercase Condition
lowcase_result = re.search(r"[a-z]", create_password)

if lowcase_result:
    # Temporary result variables used to verify each Lowercase check during testing
    lowcase_result = passed
    print("Atleast one character is Lowercase!")
else:
    lowcase_result = failed
    print("No Characters Are Lowercase")

#Numbercase Condition
numcase_result = re.search(r"[0-9]", create_password)

if numcase_result:
    # Temporary result variables used to verify each Numbercase check during testing
    numcase_result = passed
    print("Atleast one character is a number!")
else:
    numcase_result = failed
    print("No Number Characters Included")

#Special Characters Condition
special_result = re.search(special_characters, create_password)

if special_result:
    # Temporary result variables used to verify special character check during testing
    special_result = passed
    print("Atleast one special character included")
else:
    special_result = failed
    print("Special Case Not Included")

#Strength Checker - Weak, Medium, or Strong

character_score = sum([upcase_result, lowcase_result, numcase_result, special_result])

if len(create_password) >= min_length and character_score == 4:
    strength = "Strong"
elif len(create_password) >= min_length and character_score == 3:
    strength = "Medium"
else:
    strength = "Weak"
print(character_score)
print(strength)
    