INPUT = "input.txt"

with open(INPUT) as fd:
    inputs = [int(num) for num in fd.readlines()]

# part 1

last = None
count = 0
for depth in inputs:
    if last:
        if depth > last:
            count += 1
    last = depth

print(f"day 1 {count=}")

# part 2
