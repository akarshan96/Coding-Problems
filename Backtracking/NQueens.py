queens = []


def is_valid(row, col):
    if not queens:
        return True
    else:
        for queen in queens:
            if row == queen[0] or col == queen[1] or row - queen[0] == col - queen[1] or row - queen[0] == -(
                col - queen[1]):
                return False
    return True


def n_queen_util(row, n):
    if n == row:
        return True

    for i in range(n):
        if is_valid(row, i):
            queens.append((row, i))
            if n_queen_util(row + 1, n):
                return True
            queens.remove((row, i))


def solve_n_queens(n):
    if n_queen_util(0, n):
        print(queens)


solve_n_queens(8)
