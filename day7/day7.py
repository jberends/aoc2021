# uri: https://adventofcode.com/2021/day/7
import statistics

from base import get_input

"""Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose 
any horizontal position to align them all on, but the one that costs the least fuel is horizontal 
position 2: 
Move from 16 to 2: 14 fuel 
Move from 1 to 2: 1 fuel 
Move from 2 to 2: 0 fuel 
Move from 0 to 2: 2 fuel 
Move from 4 to 2: 2 fuel 
Move from 2 to 2: 0 fuel 
Move from 7 to 2: 5 fuel 
Move from 1 to 2: 1 fuel 
Move from 2 to 2: 0 fuel 
Move from 14 to 2: 12 fuel 
This costs a total of 37 fuel. This is the cheapest possible outcome; 
more expensive outcomes include aligning at 
position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel). 

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they 
spend to align to that position?
"""

file_path = get_input(7, ".txt")

INPUT = """16,1,2,0,4,2,7,1,2,14"""
INPUT = file_path.open().read()

input = [int(s) for s in INPUT.strip().split(',')]

median = int(statistics.median(input))

cost = 0
for num in input:
    cost += abs(num - median)
    
print(f"part1 cost = {cost=}")
