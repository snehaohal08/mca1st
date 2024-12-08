#15. Regular Expression Usage
#Write a program to validate email addresses using regular expressions.

import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")  
