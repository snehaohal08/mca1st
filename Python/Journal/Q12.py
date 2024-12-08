
import re
name=input("Enter the customer name : ")
email=input("Ente the eamil : ")
n=input("Enter the phone No")

def validate_email():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Email is valid...")
    else:
        print("Email is not valid")
        print("Plese enter the valid email...")

def validate_phone():
    # Validate phone number pattern
    pattern = r'^\d{10}$'
    if re.match(pattern, n):  # n is already a string
        print("Phone number is valid.")
    else:
        print("Phone number is not valid.")
        print("Enter a valid 10-digit phone number.")


def Name():
    pattern = r'([A-Z][a-z])'
    if re.match(pattern,name):
        print("Nmae is valid.....")
    else:
        print("Name is not valid.....")
        print("plese enter the valid name")


Name()
validate_email()
validate_phone()