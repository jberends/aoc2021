# uri: https://adventofcode.com/2021/day/5
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


inputs = INPUT_S.readlines()
tupes = []
for line in inputs:
    a, b = line.split(" -> ")
