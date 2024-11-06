def print_board(board):
    """Function to print the chessboard."""
    for row in board:
        print(" ".join(["Q" if cell else "." for cell in row]))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    """Place queens using backtracking."""
    if row == 8:  # All queens are placed
        return True
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at (row, col)
            if solve(board, row + 1):  # Recur to place the next queen
                return True
            board[row] = -1  # Backtrack

    return False

def eight_queens(start_row, start_col):
    """Solves the 8-Queens problem with the first queen placed at (start_row, start_col)."""
    board = [-1] * 8  # Initialize the board, where board[i] = column of the queen in row i
    board[start_row] = start_col  # Place the first queen

    if solve(board, 0):  # Start backtracking from the first row
        # Print the board where "Q" represents queens and "." represents empty spaces
        for row in range(8):
            line = ["."] * 8
            line[board[row]] = "Q"
            print(" ".join(line))
    else:
        print("No solution found")

# Example: Place the first queen at position (0, 0)
eight_queens(0, 0)
