import math
import os


def sqr_root(*args):
    a, b, c = list(map(int, args))
    if c < 0:
        print("NO SOLUTION")
    elif (a + b) == c * c and (2 * a + b) == c * c:
        print("MANY SOLUTIONS")
    else:
        if a != 0 and (c * c - b) / a == (c * c - b) // a:
            print((c * c - b) // a)
        else:
            print("NO SOLUTION")


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_sqr_root(capfd):
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        a, b, c = numbers.split('\n')
        sqr_root(a, b, c)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
