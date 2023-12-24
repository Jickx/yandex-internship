from algorithms_training_2021.lesson_2.get_input import get_input


def find_nearest_number(nums: list[int], num: int) -> None:
    nearest = 0
    nearest_diff = abs(num - nums[nearest])
    for i in range(1, len(nums)):
        if abs(num - nums[i]) < nearest_diff:
            nearest = i
            nearest_diff = abs(num - nums[i])
    print(nums[nearest])


i = input()
nums = list(map(int, input().split()))
num = int(input())
find_nearest_number(nums, num)

# def test_find_nearest_number(capfd):
#     input_lines = get_input(__name__)
#     for line in input_lines:
#         numbers, expected = line.split('\n\n')
#         message = numbers.replace('\n', ' ')
#         i, nums, num = numbers.split('\n')
#         find_nearest_number(list(map(int, nums.split())), int(num))
#         actual, err = capfd.readouterr()
#         assert actual.strip() == expected, message
