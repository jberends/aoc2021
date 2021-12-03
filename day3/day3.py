# uri: https://adventofcode.com/2021/day/3
from typing import List

from base import get_input

file_path = get_input(3, ".txt")

INPUT_S = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""



nums = [r for r in INPUT_S.splitlines()]

with file_path.open() as fd:
    nums = fd.readlines()


bin_len = len(nums[0])
nums_len = len(nums)

def most_common(ll: List[str]) -> int:
    if ll.count("1") >= len(ll) / 2:
        return 1
    return 0

gamma = ""
eps = ""
for index in range(bin_len):
    if most_common([n[index] for n in nums]):
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

gamma_dec = int(gamma, 2)
eps_dec = int(eps, 2)

print(f"part1 = {gamma_dec * eps_dec}")
