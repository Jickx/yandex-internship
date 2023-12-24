from algorithms_training_2021.lesson_2.get_input import get_input


def find_closest_number(arr, num):
    print(min(arr, key=lambda el: abs(num - el)))


# N = int(input())
# arr = list(map(int, input().split()))
# num = int(input())
#
# find_closest_number(arr, num)

def test_find_closest_number(capfd):
    input_lines = get_input(__name__)
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        i, arr, num = numbers.split('\n')
        find_closest_number(list(map(int, arr.split())), int(num))
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
