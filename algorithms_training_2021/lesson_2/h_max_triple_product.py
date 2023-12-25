def find_max_triple_product(arr: list[int]) -> tuple:
    max_num = max(arr[:3])
    max_num3 = min(arr[:3])
    max_num2 = sum(arr[:3]) - max_num3 - max_num
    for i in range(3, len(arr)):
        if arr[i] > max_num3:
            if arr[i] > max_num2:
                if arr[i] > max_num:
                    max_num3, max_num2, max_num = max_num2, max_num, arr[i]
                else:
                    max_num3, max_num2 = max_num2, arr[i]
            else:
                max_num3 = arr[i]

    min_num = min(arr[0:2])
    min_num_2 = max(arr[0:2])
    for i in range(2, len(arr)):
        if arr[i] < min_num_2:
            if arr[i] < min_num:
                min_num_2 = min_num
                min_num = arr[i]
            else:
                min_num_2 = arr[i]
    return (max_num, max_num2, max_num3) if max_num * max_num2 * max_num3 > min_num * min_num_2 * max_num else (
        max_num, min_num_2, min_num)


# print(find_max_triple_product(list(map(int, input().split()))))

assert find_max_triple_product([3, 5, 1, 7, 9, 0, 9, -3, 10]) == (10, 9, 9)
assert find_max_triple_product([-5, -30000, -12]) == (-5, -12, -30000)
assert find_max_triple_product([1, 2, 3]) == (3, 2, 1)
