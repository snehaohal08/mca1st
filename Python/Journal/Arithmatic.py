# arithmetic.py

class Addition:
    @staticmethod
    def add(a, b):
        return a + b

class Subtraction:
    @staticmethod
    def subtract(a, b):
        return a - b

class Multiplication:
    @staticmethod
    def multiply(a, b):
        return a * b

class Division:
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage
if __name__ == "__main__":
    print("Addition:", Addition.add(10, 5))
    print("Subtraction:", Subtraction.subtract(10, 5))
    print("Multiplication:", Multiplication.multiply(10, 5))
    print("Division:", Division.divide(10, 5))
