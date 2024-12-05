import re

input = open("input.txt").read()
instruction_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

# Part I
result = sum(
    [
        int(instruction.group(1)) * int(instruction.group(2))
        for instruction in instruction_pattern.finditer(input)
    ]
)
print("Part 1:")
print(result)

conditional_pattern = re.compile(r".+?(?=don?'?t?\(\)|\Z)", re.DOTALL)
memory_parts_match = conditional_pattern.findall(input)

result2 = sum(
    [
        sum(
            [
                int(instruction.group(1)) * int(instruction.group(2))
                for instruction in instruction_pattern.finditer(part)
            ]
        )
        for part in memory_parts_match
        if not part.startswith("don't()")
    ]
)
print("Part 2:")
print(result2)
