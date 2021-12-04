# uri: https://adventofcode.com/2021/day/4
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

class Board:
    dim = 5
    def __init__(self, boardlines):
        boardlines = [[int(j) for j in i] for i in boardlines]
        self.board = boardlines
        self.matches = []
        self.bingo = False


    def match(self, match:int):
        self.matches.append(match)

        for i in range(5):
            for j in range(5):
                if self.board[i][j] == match:
                    self.board[i][j] = True

    def bingo_check(self) -> bool:
        """check for bingo"""
        row = False
        column = False
        diag = False

        for i in range(5):
            if all(self.board[i]):
                self.bingo = True
                return True
            for j in range(5):



nums = [int(n) for n in INPUT.splitlines()[0].split(",")]

boardlines = [l.split() for l in INPUT.splitlines()[1:]]

boards = []
for i in range(int(len(boardlines)/6)):
    boards.append(Board(boardlines[i*6+1:i*6+6]))
pass
