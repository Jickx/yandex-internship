from get_input import get_input


def is_list_grow(*args: list[int]) -> None:
    l = []
    for arg in args:
        l.extend(arg)
    prev = l[0]
    is_valid = 'YES'
    for i in range(1, len(l)):
        if l[i] > prev:
            prev = l[i]
        else:
            is_valid = 'NO'
    print(is_valid)


# is_list_grow(list(map(int, input().split())))

def test_count_trains(capfd):
    input_lines = get_input(__name__)
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        is_list_grow(list(map(int, numbers.split(' '))))
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
