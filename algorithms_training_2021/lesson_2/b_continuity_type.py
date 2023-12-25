from algorithms_training_2021.lesson_2.get_input import get_input


def is_constant(l: list) -> bool:
    return all(l[0] == l[i] for i in range(1, len(l)))


def is_ascending(l: list) -> bool:
    return all(x <= y for x, y in zip(l, l[1:]))


def is_weakly_ascending(l: list) -> bool:
    return any(x == y for x, y in zip(l, l[1:]))


def is_descending(l: list) -> bool:
    return all(x >= y for x, y in zip(l, l[1:]))


def is_weakly_descending(l: list) -> bool:
    return any(x == y for x, y in zip(l, l[1:]))


def continuity_type(l: list[int]) -> None:
    if is_constant(l):
        cont_type = 'CONSTANT'
    elif is_ascending(l):
        cont_type = 'WEAKLY ASCENDING' if is_weakly_ascending(l) else 'ASCENDING'
    elif is_descending(l):
        cont_type = 'WEAKLY DESCENDING' if is_weakly_descending(l) else 'DESCENDING'
    else:
        cont_type = 'RANDOM'
    print(cont_type)


# data = []
# while True:
#     num = input()
#     if num == '-2000000000':
#         break
#     data.append(int(num))
#
# continuity_type(data)

def test_continuity_type(capfd):
    input_lines = get_input(__name__)
    for line in input_lines:
        numbers, expected = line.split('\n-2000000000\n')
        message = numbers.replace('\n', ' ')
        continuity_type(list(map(int, numbers.split('\n'))))
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
