#!/usr/bin/python3
import sys

# Check if the position is safe for the queen


def is_safe(board, row, col):
    # Check this column in previous rows
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Backtracking function to solve the N Queens problem


def solve_nqueens(N):
    def backtrack(row, board):
        if row == N:
            # Convert board into the desired output format
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    backtrack(0, board)
    return solutions

# Main function to handle command-line arguments and solve the problem


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Get all solutions and print them
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
