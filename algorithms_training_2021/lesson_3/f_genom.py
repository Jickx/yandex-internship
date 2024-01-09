genom_1 = input()
genom_2 = input()


a = list(''.join(x) for x in zip(genom_1, genom_1[1:]))
b = set(''.join(x) for x in zip(genom_2, genom_2[1:]))
print(sum(1 for x in a if x in b))
