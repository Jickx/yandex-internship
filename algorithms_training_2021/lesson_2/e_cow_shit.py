from algorithms_training_2021.lesson_2.get_input import get_input


def find_place(arr: list[int]) -> int:
    winner_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[winner_index]:
            winner_index = i

    score = 0
    for i in range(winner_index + 1, len(arr) - 1):
        if arr[i + 1] < arr[i] and str(arr[i])[-1] == '5' and arr[i] > score:
            score = arr[i]
    if score == 0:
        return 0

    bigger_results_count = 0
    for i in range(len(arr)):
        if arr[i] > score:
            bigger_results_count += 1
    return bigger_results_count + 1


# n = input()
# arr = list(map(int, input().split()))
# print(find_place(arr))

def test_find_place(capfd):
    input_lines = get_input(__name__)
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.split('\n')[1]
        n, arr = numbers.split('\n')
        print(find_place(list(map(int, arr.split(' ')))))
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
