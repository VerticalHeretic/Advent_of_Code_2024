from typing import List

left = []
right = []

with open("input.txt", "r") as file:
    for line in file:
        sep = line.strip().split("   ")
        left.append(int(sep[0]))
        right.append(int(sep[1]))


# Part 1
# Our main goal was to count the distance between two points in the left and right list
# The distance is counter by subtracting the smallest number in the left list from the smallest number in the right list
# and so on until the largest number in the left list, then we sum up all the distances. I've implemented it with abs value and sorting of both lists
# this way we don't have to care about the order of the numbers in the lists, and the abs value makes sure that the distance is always positive
def count_sum_of_distances(left: List[int], right: List[int]) -> int:
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    sum_distances = 0
    for i in range(len(left_sorted)):
        distance = abs(left_sorted[i] - right_sorted[i])
        sum_distances += distance
    return sum_distances


# Part 2
# Our goal was to count the sum of similarities between two lists
# The similarity is counted by multiplying the count of a number picked from the left list in the right list by the number itself
# and then summing up all the similarities. I've implemented it with a simple loop through the left list and the count method of the right list
def count_sum_of_similarities(left: List[int], right: List[int]) -> int:
    sum_similarities = 0
    for number in left:
        number_count = right.count(number)
        sum_similarities += number_count * number
    return sum_similarities


print(count_sum_of_distances(left, right))
print(count_sum_of_similarities(left, right))
