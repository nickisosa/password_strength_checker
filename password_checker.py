#This project was created to check the strength of a password
import re
print("+--------------------------------------+")
print("|       PASSWORD STRENGTH CHECKER      |")
print("+--------------------------------------+")
#General Variables
min_length = 8
special_character_pattern = r"[!@#$%&_\-*+]" 

password = input("Create a new password: ")
print("-" * 50) 

#Length Checker
length_check = len(password) >= min_length

if length_check:
    print("Minimum length requirement met.")
else:
    print("Minimum length requirement not met.")
    print("Suggestion: Use a password with at least 8 characters.")

#Uppercase Condition
upcase_search = re.search(r"[A-Z]", password)
has_uppercase = bool(upcase_search) 

if has_uppercase:
    print("Uppercase character detected.")
else:
    print("No uppercase character detected.")
    print("Suggestion: Add at least one uppercase letter.")

#Lowercase Condition
lowercase_search = re.search(r"[a-z]", password) 
has_lowercase = bool(lowercase_search) 

if has_lowercase:
    print("Lowercase character detected.")
else:
    print("No lowercase character detected.")
    print("Suggestion: Add at least one lowercase letter.")

#Numeric Character Condition
number_search = re.search(r"[0-9]", password)
has_number = bool(number_search)


if has_number:
    print("Numeric character detected.")
else:
    print("No numeric characters detected.")
    print("Suggestion: Add at least one number.")

#Special Characters Condition
special_character_search = re.search(special_character_pattern, password)
has_special_char = bool(special_character_search)


if has_special_char:
    print("Approved special character detected.")
else:
    print("No approved special character detected.")
    print("Suggestion: Add at least one approved special character.")

print("-" * 50)
#Strength Checker - Weak, Medium, or Strong
character_score = sum([has_uppercase, has_lowercase, has_number, has_special_char])

if length_check and character_score == 4:
    strength = "Strong"
elif length_check and character_score == 3:
    strength = "Medium"
else:
    strength = "Weak"
print("Character Requirements Met:", character_score, "out of 4")
print("Password Strength:", strength)
print("-" * 50)