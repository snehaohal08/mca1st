#Write a python program for exception handling with file handling operations.

file_name=input("Enter the file name : ")
fp=None
print("1. Create file and write something to it.")
print("2.read from specified file.")
print("3. append to the file")
ch=int(input("Enter your choice:"))
try:
    if ch==1:
        # 'x' mode is used to create a file and also returns an error if the file exists.
        # 'w' is used to write the file it usually overwrite the text.
        # 'w+'  is used read and write the file 
        fp=open(file_name,"x")  
        text=input("Enter the text to be written:")
        fp.write(text)
        print(f"{text} is written in {file_name}")
    elif ch==2:
        # 'r' is used to read the file.
        # 'r+' is used to read and write the file.
        fp=open(file_name,"r")
        print(fp.read())
    elif ch==3:
        # 'a' is used append.
        fp=open(file_name,'a')
        text=input("Enter the text to append.")
        fp.write(text)    

except FileNotFoundError :
    print(f"{file_name} not found")
except FileExistsError:
    print(f"{file_name} already exists")
finally :
    if fp:
        fp.close()

