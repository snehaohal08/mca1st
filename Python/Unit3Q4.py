#14. Multithreading
#Create a Python program with two threads: one to print even numbers and another to print odd numbers from a list.


import threading    
import time

def print_even_numbers():
    for i in range(2, 21, 2):
        print(i)
        time.sleep(1)

def print_odd_numbers():
    for i in range(1, 21, 2):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=print_even_numbers)
t2 = threading.Thread(target=print_odd_numbers)

t1.start()
t2.start()