# n_queens classical example of backtracking

def is_safe(board_, row, col):
    # Check this row on left side
    for i in range(row):
        if board_[i][col]:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board_[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < len(board_):
        if board_[i][j]:
            return False
        i = i + 1
        j = j - 1

    return True


def n_queens(board_: list, row: int) -> bool:
    if row == len(board_):   # base case, when we are end of row, impies all prev levels are cool
        return True
    for col in range(len(board_)):
        if is_safe(board_, row, col):
            board_[row][col] = 1
            if n_queens(board_, row + 1):  # checking for next level
                return True  # if next level is ok current level is cool
            board_[row][col] = 0  # if next level is not ok current level is not cool
    return False  # exhausted the complete columns in the row


if __name__ == '__main__':
    board = [
        [0 for _ in range(4)] for _ in range(4)
    ]

    print(n_queens(board, 0))
    for row_ in board:
        print(row_)

