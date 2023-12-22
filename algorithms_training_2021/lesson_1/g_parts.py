import os


def find_details_number(k: int, n: int, m: int) -> None:
    result = 0
    if k >= n >= m:
        while k >= n:
            n_num = k // n
            k -= n * n_num
            m_num = n // m
            rem = n - m * m_num
            k += rem * n_num
            result += m_num * n_num
        print(result)
    else:
        print(0)


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_is_number_exist(capfd):
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        k, n, m = map(int, numbers.split(' '))
        find_details_number(k, n, m)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message

# find_details_number(*map(int, input().split()))
