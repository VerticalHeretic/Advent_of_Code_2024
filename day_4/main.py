input = open("small_input.txt").read()

current_xmas = ""
xmas_count = 0

for index, character in enumerate(input):
    print(f" {index}: Current character:", character)
    print(f" {index}: Current xmas:", current_xmas)
    if current_xmas == "" and character == "X":
        current_xmas = "X"
    elif current_xmas == "X" and character == "M":
        current_xmas += "M"
    elif current_xmas == "XM" and character == "A":
        current_xmas += "A"
    elif current_xmas == "XMA" and character == "S":
        current_xmas = ""
        xmas_count += 1

print(xmas_count)
