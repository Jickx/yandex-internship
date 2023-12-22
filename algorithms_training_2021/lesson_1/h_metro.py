import os


def count_trains(a: int, b: int, n: int, m: int) -> None:
    a_min = n + a * (n - 1)
    a_max = n + a * (n + 1)
    b_min = m + b * (m - 1)
    b_max = m + b * (m + 1)

    t_min = max(a_min, b_min)
    t_max = min(a_max, b_max)

    if t_min > t_max:
        print('-1')
    else:
        print(t_min, t_max)


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_count_trains(capfd):
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        a, b, n, m = map(int, numbers.split('\n'))
        count_trains(a, b, n, m)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message


# count_trains(*map(int, [input(), input(), input(), input()]))
