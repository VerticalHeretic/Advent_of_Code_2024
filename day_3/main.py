import re

result = sum(
    int(x) * int(y)
    for line in open("input.txt")
    for x, y in re.findall(r"mul\((\d+),(\d+)\)", line)
)

print(result)