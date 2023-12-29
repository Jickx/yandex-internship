def find_sum(nums: list, x: int) -> tuple:
    nums_set = set()
    for num in nums:
        if x - num in nums_set:
            return num, x - num
        nums_set.add(num)
    return 0, 0


print(find_sum([1, 2, 3], 5))
