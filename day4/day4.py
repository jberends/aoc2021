# uri: https://adventofcode.com/2021/day/4
from typing import Optional

from base import get_input

file_path = get_input(4, ".txt")

INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

INPUT = file_path.read_text()

class Board:
    dim = 5
    def __init__(self, board):
        if len(board) < 25:
            raise AssertionError(f"length of this board is not 25: {board}, {len(board)}")
        self.board = [int(n) for n in board]
        self.matches = []

        self.bingo = False


    def match(self, match:int) -> Optional[int]:
        if match in self.board and not self.bingo:
            self.matches.append(match)
            if self.bingo_check():
                return match * self.bingo_sum_times_match

    @property
    def bingo_sum_times_match(self) -> int:
        return sum(set(self.board) - set(self.matches)) * self.matches[-1]

    def bingo_check(self) -> bool:
        """check for bingo"""
        for i in range(5):
            if all([self.board[i*5+j] in self.matches for j in range(5)]) or \
                    all([self.board[i+j*5] in self.matches for j in range(5)]):
                self.bingo = True
                return True
        return False


nums = [int(n) for n in INPUT.splitlines()[0].split(",")]

boardlines = [l.split() for l in INPUT.split("\n\n")]

boards = [Board(b) for b in boardlines[1:]]

winned_boards = []
for num in nums:
    for index, board in enumerate(boards):
        if index not in winned_boards and board.match(num):
            bingo = True
            print(f"board {index} wins: {board.bingo_sum_times_match=}")
            winned_boards.append(index)

print(f"{sorted(winned_boards)=}")
print(set([n for n in range(len(boards))])-set(winned_boards))
