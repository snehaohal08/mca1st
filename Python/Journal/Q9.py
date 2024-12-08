# Write a function for the armstrong number, palindrome, prime number using the switch case

def Airmstrong():
    n=int(input("Enter the no: "))
    print("***********************************************")
    sum=0
    temp=n
    while temp>0:
        r=temp%10
        sum += r**3
        temp //=10
    if n==sum:
        print("No is Armstrong....")
        
    else:
        print("No is not Armstrong.")
        

def Pailondrom():
    n=int(input("Enter the No: "))
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        print("No is pailondrom..........")
        print("***********************************************")
    else:
        print("No is not pailondrom..........")
        print("***********************************************")
def Prim(): 
    a=int(input("Enter number: "))
    k=0
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a %i==0:
            return False
        return True
    if(a):
        print("Number is prime")
        print("***********************************************")
    else:
        print("Number is not prime")
        print("***********************************************")
def menu():
    while True:
        print("1.Airmstrong\n2.Pailondrom\n3.Prim\n4.Exit")
        ch=int(input("Enter the choice: "))
        match ch:
            case 1:
                Airmstrong()
            case 2:
                Pailondrom()
            case 3:
                Prim()
            case 4:
                exit
                break
            case _:
                print("Invalid choice..............")
menu()