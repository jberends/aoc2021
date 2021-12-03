# uri: https://adventofcode.com/2021/day/2
from ..base import get_input

inputs_string = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

file_path = get_input(2, ".txt")

with file_path.open() as fd:
    inputs = [row.split(" ") for row in fd.readlines()]
# inputs = [row.split(" ") for row in inputs_string.splitlines()]

pos = 0
depth = 0

for row in inputs:
    command, amount = row

    if command == "forward":
        pos += int(amount)
    elif command == "down":
        depth += int(amount)
    elif command == "up":
        depth -= int(amount)
    else:
        raise ValueError(f"We fell through the if loop: {command=}, {amount=}")

result = pos * depth
print(f"part 1 {result}")

# part 2


pos = 0
depth = 0
aim = 0

for row in inputs:
    command, amount = row

    if command == "forward":
        pos += int(amount)
        depth += aim * int(amount)
    elif command == "down":
        aim += int(amount)
    elif command == "up":
        aim -= int(amount)
    else:
        raise ValueError(f"We fell through the if loop: {command=}, {amount=}")

result = pos * depth
print(f"part 2 {result}")
