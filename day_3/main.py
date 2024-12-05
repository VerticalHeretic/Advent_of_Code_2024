import re
import ast

all_multiplication_numbers = []

for line in open("input.txt", "r"):
    all_multiplication_numbers.extend(re.findall(r"mul\((\d+),(\d+)\)", line))

result = 0
for tuple_string in all_multiplication_numbers:
    # tuple_string.strip("()")
    # tuple_string = tuple_string.split(",")
    number1, number2 = map(int, tuple_string)
    result += number1 * number2

print(result)
