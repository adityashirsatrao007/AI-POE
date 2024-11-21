def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j]:
                return False
        return True

    def solve(board, col):
        if col >= n:
            solutions.append(["".join('Q' if c else '.' for c in row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = True
                solve(board, col + 1)
                board[i][col] = False

    solutions = []
    board = [[False] * n for _ in range(n)]
    solve(board, 0)
    return solutions

# Example Usage
solutions = solve_n_queens(8)
for sol in solutions:
    print("\n".join(sol), "\n")
