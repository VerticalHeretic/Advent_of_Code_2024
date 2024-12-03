def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


data = [[int(y) for y in x.split(" ")] for x in open("input.txt").read().split("\n")]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

# Calculate the total number of rows that are considered "safe" by checking
# if removing any single element from the row results in a safe configuration.
safe_count = sum(
    [
        # For each row, check if removing any single element makes it safe
        any(
            [
                # Create a new list without the element at index i
                # and check if it's safe
                is_safe(row[:i] + row[i + 1 :])
                for i in range(len(row))
            ]
        )
        for row in data
    ]
)
# Print the total count of rows that can be made safe by removing one element
print(safe_count)
