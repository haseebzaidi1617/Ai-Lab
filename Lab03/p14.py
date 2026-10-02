import re

password = input("Enter your password: ")
if len(password) < 6:
    print("Password must be at least 6 characters long.")   
if len(password) > 16:
    print("Password must be at most 16 characters long.")

is_valid = True

if not (6 <= len(password) <= 16):
    is_valid = False
elif not re.search("[a-z]", password):
    is_valid = False
elif not re.search("[A-Z]", password):
    is_valid = False
elif not re.search("[0-9]", password):
    is_valid = False
elif not re.search("[$#@]", password):
    is_valid = False

if is_valid:
    print("Valid Password")
else:
    print("Invalid Password")