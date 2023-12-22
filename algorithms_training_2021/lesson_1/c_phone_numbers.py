import os

ANSWERS = {
    True: 'YES',
    False: 'NO'
}


def format_num(num: str) -> str:
    number = ''.join([i for i in num if i.isdigit()])
    if len(number) > 7:
        code = number[-10:-7]
    else:
        code = '495'
    digits = number[-7:]
    return code + digits


def is_number_exist(new_num: str, *args: str) -> None:
    new_num = format_num(new_num)
    nums = list(map(format_num, args))
    for num in nums:
        print(ANSWERS[new_num == num])


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_is_number_exist(capfd):
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        new_num, num1, num2, num3 = numbers.split('\n')
        is_number_exist(new_num, num1, num2, num3)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
