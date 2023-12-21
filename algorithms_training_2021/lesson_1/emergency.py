import os


def find_address(*args):
    apt1, floors, apt2, entr2, floor2 = list(map(int, args))
    apps_on_floor = apt2 / (floors * (entr2 - 1) + floor2)
    if apps_on_floor % 1 != 0:
        apps_on_floor += 1
    apps_on_floor = int(apps_on_floor)
    apps_on_entr = floors * apps_on_floor
    entr1 = (apt1 // apps_on_entr) + 1
    floor1 = ((apt1 - (apps_on_entr * (entr1 - 1))) // apps_on_floor) + 1
    if floor2 < 2:
        entr1 = 1
    if apt1 < floors:
        entr1 = 1
    if floor2 > apt2 or floor2 > floors or floor2 < entr2:
        print('-1 -1')
    else:
        print(entr1, floor1)


path = os.path.join('input', __name__)
with open(path, 'r') as f:
    input_lines = f.read().strip().split('\n\n\n')


def test_sqr_root(capfd):
    for line in input_lines:
        numbers, expected = line.split('\n\n')
        message = numbers.replace('\n', ' ')
        app1, floors, app2, entr2, floor2 = numbers.split(' ')
        find_address(app1, floors, app2, entr2, floor2)
        actual, err = capfd.readouterr()
        assert actual.strip() == expected, message
