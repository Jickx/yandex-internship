name = input()

is_dig, is_lower, is_upper = False, False, False

for i in name:
    if i.isdigit():
        is_dig = True
    if i.islower():
        is_lower = True
    if i.isupper():
        is_upper = True

if len(name) >= 8 and is_dig and is_lower and is_upper:
    print('YES')

else:
    print('NO')
