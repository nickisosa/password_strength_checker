#This project was created to check the strength of a password
import re

#General Variables
user_password = input("Create a new password: ")
min_length = 8
max_strength = 20
passed = True
failed = False
special_characters = r"[!@#$%&_\-*+]"

#Length Checker
if len(user_password) >= min_length:
    length_check = passed
    print("Length Check Satisfied")
else:
    length_check = failed
    print("Length Check Not Satisfied")

#Uppercase Condition
uppercase_check = re.search(r"[A-Z]", user_password)

if uppercase_check:
    upcase_result = passed
    print("Atleast one Character is Uppercase!")
else:
    upcase_result = failed
    print("No Characters Are Uppercase")

#Lowercase Condition
lowercase_check = re.search(r"[a-z]", user_password)

if lowercase_check:
    lowcase_result = passed
    print("Atleast one character is Lowercase!")
else:
    lowcase_result = failed
    print("No Characters Are Lowercase")

#Numbercase Condition
numbercase_check = re.search(r"[0-9]", user_password)

if numbercase_check:
    numcase_result = passed
    print("Atleast one character is a number!")
else:
    numcase_result = failed
    print("No Number Characters Included")

#Special Characters Condition
search_char = re.search(special_characters, user_password)

if search_char:
    special_result = passed
    print("Atleast one special character included")
else:
    special_result = failed
    print("Special Case Not Included")