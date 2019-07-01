path = []
n = 4
m = 4


def is_valid(arr, x, y):
    if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
        return True
    return False


def maze_util(arr, x, y):
    if x == n - 1 and y == n - 1:
        return True

    if is_valid(arr, x, y):
        path.append((x, y))
        if maze_util(arr, x + 1, y):
            return True

        if maze_util(arr, x, y + 1):
            return True
        path.remove((x, y))
        return False


def solve_maze():
    arr = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    maze_util(arr, 0, 0)

solve_maze()
print path
