from algorithms_training_2021.lesson_2.get_input import get_input


def find_bigger_neighbours(arr: list[int]) -> int:
    return sum(1 for i in range(1, len(arr) - 1) if arr[i - 1] < arr[i] > arr[i + 1])


# print(find_bigger_neighbours(list(map(int, input().split()))))

def test_biggest_neighbours(capfd):
    input_lines = get_input(__name__)
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        print(find_bigger_neighbours(list(map(int, numbers.split()))))
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
