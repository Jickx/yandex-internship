import os

# troom, tcond = list(map(int, input().split()))
# mode = input()


path = os.path.join('input', 'air_con')
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')

print(input_lines)


def change_temp(troom, tcond, mode):
    if mode == 'fan':
        print(troom)
    elif mode == 'heat' and troom <= tcond:
        print(tcond)
    elif mode == 'heat' and troom > tcond:
        print(troom)
    elif mode == 'freeze' and troom >= tcond:
        print(tcond)
    elif mode == 'freeze' and troom < tcond:
        print(troom)
    elif mode == 'auto':
        print(tcond)


def test_change_temp(capfd):
    for line in input_lines:
        temp, mode, _, expected = line.split('\n')
        troom, tcond = temp.split()
        change_temp(int(troom), int(tcond), mode)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected
