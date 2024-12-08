import threading
import time

def print_numbers(num):
    for i in range(1, num + 1):
        print("The numbers are:", i)

def print_cube(num):
    for i in range(1, num + 1):
        print("Cube of", i, "is:", i * i * i)

def print_square(num):
    for i in range(1, num + 1):
        print("Square of", i, "is:", i * i)

if __name__ == "__main__":
    # Creating threads
    t1 = threading.Thread(target=print_numbers, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))
    t3 = threading.Thread(target=print_cube, args=(10,))
    

    # Starting thread 1
    t1.start()
    time.sleep(1.5)
    t1.join()  # Wait for t1 to complete before starting t2
    print("😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰")


    # Starting thread 2
    t2.start()
    time.sleep(1.5)
    t2.join()  # Wait for t2 to complete before starting t3
    print("😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰")

    # Starting thread 3
    t3.start()
    time.sleep(1.5)
    t3.join()  # Wait for t3 to complete before ending the program
    print("😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰😍🥰")
