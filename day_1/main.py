left = []
right = []
with open("day1.txt", "r") as file:
    for line in file:
        sep = line.strip().split("   ")
        left.append(sep[0])
        right.append(sep[1])

left_sorted = sorted(map(int, left))
right_sorted = sorted(map(int, right))

sum_distances = 0
for i in range(len(left_sorted)):
    distance = abs(left_sorted[i] - right_sorted[i])
    sum_distances += distance

print(sum_distances)
