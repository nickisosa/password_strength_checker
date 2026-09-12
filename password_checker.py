#This project was created to check the strength of a password
import re
print("+--------------------------------------+")
print("|       PASSWORD STRENGTH CHECKER      |")
print("+--------------------------------------+")
#General Variables
min_length = 8
approved_characters = r"[!@#$%&_\-*+]" 

create_password = input("Create a new password: ")
print("*" * 65) 

#Length Checker
length_check = len(create_password) >= min_length

if length_check:
    print("Minimum length requirement met.")
else:
    print("Minimum length requirement not met.")
    print("Suggestion: Use a password with at least 8 characters.")
print("-" * 65)

#Uppercase Condition
upcase_search = re.search(r"[A-Z]", create_password)
has_uppercase = bool(upcase_search) 

if has_uppercase:
    print("Uppercase character detected.")
else:
    print("No uppercase character detected.")
    print("Suggestion: Add at least one uppercase letter.")
print("-" * 50)

#Lowercase Condition
lowcase_search = re.search(r"[a-z]", create_password) 
has_lowcase = bool(lowcase_search) 

if has_lowcase:
    print("Lowercase character detected!")
else:
    print("No lowercase character detected!")
    print("Suggestion: Add at least one lowercase letter.")
print("-" * 50)

#Numbercase Condition
numcase_search = re.search(r"[0-9]", create_password)
has_numbers = bool(numcase_search)


if has_numbers:
    print("Numeric character detected.!")
else:
    print("No numeric characters detected.")
    print("Suggestion: Add at least one number.")
print("-" * 50)

#Special Characters Condition
special_char_search = re.search(approved_characters, create_password)
has_special_char = bool(special_char_search)


if has_special_char:
    print("Approved special character detected.")
else:
    #print(failed)
    print("No approved special character detected.")
    print("Suggestion: Add at least one approved special character(s).")
print("-" * 65)

#Strength Checker - Weak, Medium, or Strong
character_score = sum([has_uppercase, has_lowcase, has_numbers, has_special_char])

if length_check and character_score == 4:
    strength = "Strong"
elif length_check and character_score == 3:
    strength = "Medium"
else:
    strength = "Weak"
print("Character Requirement Met:", character_score, "out of 4")
print("Password Strength:", strength)
    