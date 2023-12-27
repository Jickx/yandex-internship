def get_sides_to_count(x: int, y: int) -> dict:
    sides_to_count = {'left': (x, y - 1),
                      'right': (x, y + 1),
                      'up': (x - 1, y),
                      'down': (x + 1, y),
                      'left_up': (x - 1, y - 1),
                      'right_up': (x - 1, y + 1),
                      'right_down': (x + 1, y + 1),
                      'left_down': (x + 1, y - 1)
                      }
    sides_to_remove = set()
    if x == 0:
        sides_to_remove.update(['left_up', 'up', 'right_up'])
    if y == 0:
        sides_to_remove.update(['left_up', 'left', 'left_down'])
    if x >= n - 1:
        sides_to_remove.update(['left_down', 'down', 'right_down'])
    if y >= m - 1:
        sides_to_remove.update(['right_up', 'right', 'right_down'])
    for side in sides_to_remove:
        sides_to_count.pop(side, None)
    return sides_to_count


def create_minesweeper(n: int, m: int, mines: list[tuple]) -> list[list[int]]:
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for x, y in mines:
        sides_to_count = get_sides_to_count(x, y)
        for side in sides_to_count.values():
            i, j = side
            matrix[i][j] += 1

    for x, y in mines:
        matrix[x][y] = '*'

    return matrix


n, m, k = map(int, input().split())
mines_coordinates = []
for _ in range(k):
    mines_coordinates.append(tuple(map(lambda x: int(x) - 1, input().split())))

result = create_minesweeper(n, m, mines_coordinates)
for line in result:
    print(' '.join(map(str, line)))
