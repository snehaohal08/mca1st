# Using at least 6 special character sequence  create matching patterns

import re

# Example 1: Matching digits (\d)
pattern1 = r"\d+"
text1 = "Order number: 12345"
result1 = re.findall(pattern1, text1)
print("Digits:", result1)

# Example 2: Matching word boundaries (\b)
pattern2 = r"\bcat\b"
text2 = "The cat sat on the mat."
result2 = re.findall(pattern2, text2)
print("Word boundaries:", result2)

# Example 3: Matching whitespace (\s)
pattern3 = r"\s+"
text3 = "This is a test."
result3 = re.findall(pattern3, text3)
print("Whitespace:", result3)

# Example 4: Matching non-word characters (\W)
pattern4 = r"\W+"
text4 = "Hello, world!"
result4 = re.findall(pattern4, text4)
print("Non-word characters:", result4)

# Example 5: Matching beginning of string (^) and specific characters
pattern5 = r"^Hello"
text5 = "Hello, world! Welcome to Python."
result5 = re.findall(pattern5, text5)
print("Beginning of string:", result5)

# Example 6: Matching repeated patterns (\w{3})
pattern6 = r"\w{3}"
text6 = "abc def 123 xyz"
result6 = re.findall(pattern6, text6)
print("Repeated patterns:", result6)
