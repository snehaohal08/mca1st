from pymongo import MongoClient
Client=MongoClient("localhost:27017")
db=Client.EmpData
print("database is created")
def insert():
    try:
        eid=input("Enter the ID: ")
        ename=input("Enter the emp name: ")
        salary=input("Enter the salary: ")
        addr=input("Enter the Address: ")
        db.employee1.insert_one({
            "ID":eid,
            "E_name":ename,
            "Salary":salary,
            "Address":addr
        })
        print("Data iserted succsessfully............")
    except Exception as e:
        print("Eroor can occure.")
def duplicate_value():
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$ID",  
                    "count": {"$sum": 1},  
                    "records": {"$push": "$$ROOT"}  
                }
            },
            {
                "$match": {
                    "count": {"$gt": 1}  
                }
            }
        ]

        duplicate = list(db.employee1.aggregate(pipeline))
        if duplicate:
            print("Duplicate records are found:")
            for dup in duplicate:
                print("Employee ID: ", dup["_id"])
                for record in dup["records"]:
                    print(record)
        else:
            print("No duplicate records are found.")
    except Exception as e:
        print("An error occurred:")
        
def search_employee():
    eid=input("Enter the emp id to serach: ")
    result = db.employee1.find_one({"ID": eid})
    if result:
        print("Employee Found:", result)
    else:
        print("Employee not found.")
def delete():
    try:
        eid=input("Enter the emp id to deleted: ")
        result=db.employee1.delete_one({"ID":eid})
        if result.deleted_count>0:
            print("Employee record deleted.....")
        else:
            print("Employee is not found......")
    except Exception as e:
        print("error can occur........")


def menu():
    while True:
        print("1.Create\n2.Duplicate value\n3.Serch\n4.Delete\n5.Exit")
        ch=int(input("Enter the choice: "))
        match ch:
            case 1:
                insert()
            case 2:
                duplicate_value()
            case 3:
                search_employee()
            case 4:
                delete()
            case 5:
                exit
                break
            case _:
                print("Invalid choice..............")
menu()


# # insert()
# search_employee()
# duplicate_value()
# delete()