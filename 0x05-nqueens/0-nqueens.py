#!/usr/bin/python3
"""Solves the N-Queens problem by printing all possible solutions."""
import sys

# Validate number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Validate N is a number
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

# Convert N and validate range
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

def queens(n, row=0, rows=None, diag1=None, diag2=None):
    """Generate all valid queen placements using backtracking."""
    if rows is None:
        rows = []
    if diag1 is None:
        diag1 = []
    if diag2 is None:
        diag2 = []
    if row == n:
        # Yield solution as list of [row, col] pairs
        yield [[i, rows[i]] for i in range(n)]
    else:
        for col in range(n):
            if (col not in rows and
                    row + col not in diag1 and
                    row - col not in diag2):
                yield from queens(n, row + 1, rows + [col],
                                 diag1 + [row + col], diag2 + [row - col])

def solve(n):
    """Print all solutions to the N-Queens problem."""
    for solution in queens(n):
        print(solution)

# Run the solver
solve(n)