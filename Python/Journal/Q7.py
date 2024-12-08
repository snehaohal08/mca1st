# Demonstrating Generators

def number_generator(n):
    """A generator function that yields numbers from 0 to n."""
    for i in range(n + 1):
        yield i

# Using the generator
print("Generator output:")
for number in number_generator(5):
    print(number, end=' ')

# Demonstrating Decorators

def my_decorator(func):
    """A simple decorator that prints a message before and after the function call."""
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """A function that prints a hello message."""
    print(f"Hello, {name}!")

# Using the decorated function
print("\nDecorated function output:")
say_hello("Alice")

# Combining Generators and Decorators
@my_decorator
def generate_squares(n):
    """A generator function that yields squares of numbers from 0 to n."""
    for i in range(n + 1):
        yield i * i

# Using the decorated generator
print("\nDecorated generator output:")
for square in generate_squares(5):
    print(square, end=' ')
