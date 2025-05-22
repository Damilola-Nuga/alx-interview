#!/usr/bin/python3
""" N queens """
import sys

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is a number
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

# Convert N to integer and check if N >= 4
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

def queens(n, row=0, rows=[], diag1=[], diag2=[]):
    """ Generator function to find all possible queen placements """
    if row == n:
        # Yield the solution as a list of [row, col] pairs
        yield [[i, rows[i]] for i in range(n)]
    else:
        for col in range(n):
            # Check if the current position is safe
            if col not in rows and (row + col) not in diag1 and (row - col) not in diag2:
                # Recursively try placing queens in the next rows
                yield from queens(n, row + 1, rows + [col], diag1 + [row + col], diag2 + [row - col])

def solve(n):
    """ Solve the N-Queens problem and print all solutions """
    for solution in queens(n):
        print(solution)

# Run the solver
solve(n)