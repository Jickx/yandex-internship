def place_notebooks(a, b, c, d) -> None:
    sides = {
        'a': a,
        'b': b,
        'c': c,
        'd': d
    }
    squares = {
        'acbd': (a + c) * max(b, d),
        'adbc': (a + d) * max(b, c),
        'bcad': (b + c) * max(a, d),
        'bdac': (b + d) * max(a, c),
    }

    min_square = min(squares, key=squares.get)
    min_square = [i for i in min_square]
    hor = sides[min_square[0]] + sides[min_square[1]]
    ver = max(sides[min_square[2]], sides[min_square[3]])

    print(hor, ver)


place_notebooks(10, 2, 2, 10)
# 20 2
# 2 20
# 4 10
# 10 4

place_notebooks(5, 7, 3, 2)
# 9 5
# 5 9
