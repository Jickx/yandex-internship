import os


def is_valid_triangle(a: int, b: int, c: int) -> None:
    if a + b > c and a + c > b and c + b > a:
        print('YES')
    else:
        print('NO')


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_is_valid_triangle(capfd):
    for line in input_lines:
        sides, expected = line.split('\n\n')
        message = sides.replace('\n', ' ')
        a, b, c = list(map(int, sides.split('\n')))
        is_valid_triangle(a, b, c)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
