# uri: https://adventofcode.com/2021/day/5
import collections

from base import get_input

file_path = get_input(5, ".txt")

INPUT_S = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

inputs = INPUT_S.splitlines()
# inputs = file_path.open().readlines()

field = collections.Counter()
for line in inputs:
    f, t = line.split(" -> ")
    fx_s, fy_s = f.split(",")
    tx_s, ty_s = t.split(",")
    fx, fy, tx, ty = int(fx_s), int(fy_s), int(tx_s), int(ty_s)

    if fx != tx and fy == ty:
        # horizontal expansion
        for x in range(min((fx, tx)), max((fx, tx))+1):
            field[(x, fy)] += 1
    elif fx == tx and fy != ty:
        # vertical expansion
        for y in range(min((fy, ty)), max((fy, ty))+1):
            field[(fx, y)] += 1
    else:
        pass

# for i in range(9+1):
#     for j in range(9+1):
#         print(field.get((i, j),"."), end="")
#     print('')

counter = 0
for pos, val in field.items():
    if val >= 2:
        counter+=1
        
print(f"part1 {counter=}")


# part 2
# add diagonal lines @ 45 deg

field = collections.Counter()
for line in inputs:
    f, t = line.split(" -> ")
    fx_s, fy_s = f.split(",")
    tx_s, ty_s = t.split(",")
    fx, fy, tx, ty = int(fx_s), int(fy_s), int(tx_s), int(ty_s)

    if fx != tx and fy == ty:
        # horizontal expansion
        for x in range(min((fx, tx)), max((fx, tx))+1):
            field[(x, fy)] += 1
    elif fx == tx and fy != ty:
        # vertical expansion
        for y in range(min((fy, ty)), max((fy, ty))+1):
            field[(fx, y)] += 1
    elif abs(tx-fx) == abs(ty-fy):
        # diagonal
        ...
        print(f"diag {fx, fy} -> {tx,ty}")
        
    else:
        # non diagonal lines
        pass

# for i in range(9+1):
#     for j in range(9+1):
#         print(field.get((i, j),"."), end="")
#     print('')


