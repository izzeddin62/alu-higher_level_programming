#!/usr/bin/python3
"""searches all the solution for the n queen puzzle"""
import argparse
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isnumeric():
    print("N must be a number")
    exit(1)
if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(argv[1])
col = []
neg_diag = []
pos_diag = []
result = []
board = []


def find_queen_position(r):
    """find the queen position using backtracking"""
    if r == n:
        result.append(board[:])
        return
    for c in range(n):
        if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
            continue
        board.append([r, c])
        col.append(c)
        pos_diag.append(r + c)
        neg_diag.append(r - c)
        find_queen_position(r + 1)
        board.remove([r, c])
        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)


if __name__ == "__main__":
    find_queen_position(0)
    for i in result:
        print(i)
