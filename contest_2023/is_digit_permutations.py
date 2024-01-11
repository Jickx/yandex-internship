def count_sort(num):
    seq = [0] * 10
    while num > 0:
        last_digit = num % 10
        seq[last_digit] += 1
        num //= 10
    return seq


def is_digit_permutations(x, y):
    sorted_x = count_sort(x)
    sorted_y = count_sort(y)
    print(sorted_y, sorted_x)
    return sorted_x == sorted_y


assert is_digit_permutations(2021, 1022) is True
assert is_digit_permutations(4321, 2341) is True
assert is_digit_permutations(1002, 3001, ) is False
