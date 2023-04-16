# https://contest.yandex.ru/contest/28412/problems/B/

rows_matrix = []
letters = ['A', 'B', 'C', '_', 'D', 'E', 'F']
groups = []
answer = []
DOT = '.'
X = 'X'
DASH = '#'

number_of_rows = int(input())

for _ in range(number_of_rows):
    rows_matrix.append(input())

number_of_groups = int(input())

for _ in range(number_of_groups):
    groups.append(input().split())


def is_seat_available(row, side, num_of_persons, position):
    dots = DOT * num_of_persons
    if side == 'left' and position == 'aisle':
        return row[3 - num_of_persons:3] == dots
    elif side == 'left' and position == 'window':
        return row[0:num_of_persons] == dots
    elif side == 'right' and position == 'aisle':
        return row[4:4 + num_of_persons] == dots
    elif side == 'right' and position == 'window':
        return row[7 - num_of_persons:] == dots


def get_available_seat(row, side, num_of_persons, position):
    row_list = [char for char in row]
    exes = X * num_of_persons
    if side == 'left' and position == 'aisle':
        row_list[3 - num_of_persons:3] = exes
    elif side == 'left' and position == 'window':
        row_list[0:num_of_persons] = exes
    elif side == 'right' and position == 'aisle':
        row_list[4:4 + num_of_persons] = exes
    elif side == 'right' and position == 'window':
        row_list[7 - num_of_persons:8] = exes
    return ''.join(row_list)


def get_row(rows_matrix, side, num_of_persons, position):
    found = False
    new_matrix = []
    for i, row in enumerate(rows_matrix):
        if is_seat_available(row, side, num_of_persons, position) and not found:
            new_matrix.append(get_available_seat(
                row, side, num_of_persons, position))
            found = True
        else:
            new_matrix.append(row)
    return found, new_matrix


def check_group(group, rows_matrix):
    num_of_persons = int(group[0])
    side = group[1]
    position = group[2]
    get_row(rows_matrix, side, num_of_persons, position)
    return get_row(rows_matrix, side, num_of_persons, position)


def replace_x(rows_matrix):
    new_matrix = [item.replace(X, DASH) for item in rows_matrix]
    return new_matrix


def get_seat_letters(row_matrix, letters):
    for num, row in enumerate(row_matrix):
        if X in row:
            indexes = [pos for pos, char in enumerate(row) if char == X]
            seat_letters = [f"{num + 1}{letters[i]}" for i in indexes]
            return seat_letters
    return None


def get_seats(groups, rows_matrix):
    result = []
    for group in groups:
        found, rows_matrix = check_group(group, rows_matrix)
        if found:
            seat_letters = get_seat_letters(rows_matrix, letters)
            result.append(f"Passengers can take seats: {' '.join(seat_letters)}")
            result.extend(rows_matrix)
            rows_matrix = replace_x(rows_matrix)
        else:
            result.append('Cannot fulfill passengers requirements')

    return result

print('\n'.join(get_seats(groups, rows_matrix)))

# with open('output.txt', 'w') as f:
#     f.write('\n'.join(get_seats(groups, rows_matrix)))