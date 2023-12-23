from algorithms_training_2021.lesson_2.get_input import get_input


def is_constant(l: list) -> bool:
    prev = l[0]
    for i in range(1, len(l)):
        if l[i] != prev:
            return False
    return True


def is_ascending(l: list) -> bool:
    prev = l[0]
    for i in range(1, len(l)):
        if l[i] < prev:
            return False
        prev = l[i]
    return True


def is_weakly_ascending(l: list) -> bool:
    prev = l[0]
    for i in range(1, len(l)):
        if prev == l[i]:
            return True
        prev = l[i]
    return False


def is_descending(l: list) -> bool:
    prev = l[0]
    for i in range(1, len(l)):
        if l[i] > prev:
            return False
        prev = l[i]
    return True


def is_weakly_descending(l: list) -> bool:
    prev = l[0]
    for i in range(1, len(l)):
        if prev == l[i]:
            return True
        prev = l[i]
    return False


def continuity_type(l: list[int]) -> None:
    if is_constant(l):
        cont_type = 'CONSTANT'
    elif is_ascending(l):
        if is_weakly_ascending(l):
            cont_type = 'WEAKLY ASCENDING'
        else:
            cont_type = 'ASCENDING'
    elif is_descending(l):
        if is_weakly_descending(l):
            cont_type = 'WEAKLY DESCENDING'
        else:
            cont_type = 'DESCENDING'
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
