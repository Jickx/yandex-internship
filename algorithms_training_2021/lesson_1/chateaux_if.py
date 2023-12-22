def sort_two_sizes(a: int, b: int) -> tuple[int, int]:
    if a > b:
        return b, a
    return a, b


def is_big_enough(a: int, b: int, c: int, d: int, e: int) -> None:
    a, b = sort_two_sizes(a, b)
    b, c = sort_two_sizes(b, c)
    a, b = sort_two_sizes(a, b)
    d, e = sort_two_sizes(d, e)
    if a > d or b > e:
        print('NO')
    else:
        print('YES')


is_big_enough(*map(int, [input(), input(), input(), input(), input()]))
