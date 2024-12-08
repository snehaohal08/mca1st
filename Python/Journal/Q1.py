import pymongo
import re

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["python"]
collection = db["employee"]

# Function to check if an ID already exists in the database
def id_exists(employee_id):
    return collection.find_one({"e_id": employee_id}) is not None

# Function to validate email
def validate_email(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(regex, email) is not None

# Function to validate name
def validate_name(name):
    regex = r'^[A-Za-z\s]+$'
    return re.fullmatch(regex, name) is not None

# Function to validate mobile number
def validate_mobile(mobile):
    regex = r'^\d{10}$'
    return re.fullmatch(regex, mobile) is not None

# Collecting employee details with validations
def get_employee_details():
    while True:
        try:
            e_id = int(input("Enter Employee ID: "))
            if id_exists(e_id):
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric Employee ID.")

    while True:
        e_name = input("Enter Employee Name: ").strip()
        if validate_name(e_name):
            break
        print("Invalid name. Please enter a valid name (letters and spaces only).")

    while True:
        e_email = input("Enter Employee Email: ").strip()
        if validate_email(e_email):
            break
        print("Invalid email. Please enter a valid email address.")

    while True:
        e_mobile = input("Enter Employee Mobile: ").strip()
        if validate_mobile(e_mobile):
            break
        print("Invalid mobile number. Please enter a valid 10-digit mobile number.")

    e_dept = input("Enter Employee Department: ").strip()

    while True:
        try:
            e_salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")

    return {
        "e_id": e_id,
        "e_name": e_name,
        "e_email": e_email,
        "e_mobile": e_mobile,
        "e_dept": e_dept,
        "e_salary": e_salary
    }

# Main program
if __name__ == "__main__":
    print("Employee Registration System\n")
    employee_data = get_employee_details()
    collection.insert_one(employee_data)
    print("\nEmployee data has been successfully added to the database.")

    print("\nAll Employees in Database:")
    for user in collection.find():
        print(user)