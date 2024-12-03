safe = 0
unsafe = 0

with open("input.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split(" ")))

        levels = []
        for index in range(len(numbers) - 1):
            if (
                abs(numbers[index] - numbers[index + 1]) >= 1
                and abs(numbers[index] - numbers[index + 1]) <= 3
            ):
                levels.append(numbers[index] - numbers[index + 1])
            else:
                print("This is not safe, breaking out of the numbers loop")
                break

        print("Checking if all growing or desceing")
        if all(level > 0 for level in levels):
            safe += 1
        elif all(level < 0 for level in levels):
            safe += 1
        else:
            unsafe += 1

print(safe, unsafe)
