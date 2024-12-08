from Arithmatic import Addition, Subtraction, Multiplication, Division

# Example usage
result_add = Addition.add(15, 10)
result_sub = Subtraction.subtract(15, 5)
result_mul = Multiplication.multiply(3, 7)
try:
    result_div = Division.divide(10, 0)  # This will raise an error
except ValueError as e:
    print(e)

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_sub}")
print(f"Multiplication Result: {result_mul}")
