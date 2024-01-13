import sys
from collections import defaultdict

lines = sys.stdin.readlines()

db = defaultdict(int)


def make_operation(operation, data):
    if operation == 'INCOME':
        amount = data.strip()
        for lastname in db.keys():
            if db[lastname] > 0:
                db[lastname] += int(db[lastname] * int(amount) / 100)
    elif operation == 'DEPOSIT':
        lastname, amount = data.split()
        db[lastname] += int(amount)
    elif operation == 'WITHDRAW':
        lastname, amount = data.split()
        db[lastname] -= int(amount)
    elif operation == 'TRANSFER':
        sender, recipient, amount = data.split()
        db[sender] -= int(amount)
        db[recipient] += int(amount)
    elif operation == 'BALANCE':
        lastname = data.strip()
        if db.get(lastname) is not None:
            print(db[lastname])
        else:
            print('ERROR')


for line in lines:
    operation, data = line.split(' ', 1)
    make_operation(operation, data)
