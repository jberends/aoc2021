# uri: https://adventofcode.com/2021/day/6
import collections

"""
So, suppose you have a lanternfish with an internal timer value of 3:

After one day, its internal timer would become 2.
After another day, its internal timer would become 1.
After another day, its internal timer would become 0.
After another day, its internal timer would reset to 6, and it 
would create a new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal 
timer of 5, and the second lanternfish would have an internal timer of 7.
"""

from base import get_input

file_path = get_input(6, ".txt")

INPUT = """3,4,3,1,2"""
INPUT = file_path.open().read()

input = [int(s) for s in INPUT.strip().split(",")]

nums = collections.Counter(input)

for _ in range(256):
    # check if the counter = 0 -> than add a 6 and a 8.
    nums2 = collections.Counter({6: nums[0], 8: nums[0], 0:0})
    for k,v in nums.items():
        if k > 0:
            nums2[k-1] += v 
    nums = nums2

count = sum(nums.values())
print(f"fish count {count=}, {nums=}")

