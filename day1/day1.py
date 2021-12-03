# url: https://adventofcode.com/2021/day/1

INPUT = "input1.txt"

with open(INPUT) as fd:
    inputs = [int(num) for num in fd.readlines()]

# example
# inputs = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263,
# ]

# part1b
count = 0
for index in range(len(inputs) - 1):
    if inputs[index + 1] > inputs[index]:
        count += 1

print(f"day 1 {count=}")

# part 2
count = 0
for index in range(len(inputs) - 1):
    if sum(inputs[index + 1:index + 4]) > sum(inputs[index:index + 3]):
        count += 1

print(f"day 2 {count=}")
