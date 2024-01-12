import sys

s = sys.stdin.read().split()
dct = {}
result = []

for i in s:
    dct[i] = dct.get(i, 0)
    result.append(dct[i])
    dct[i] += 1

print(' '.join(map(str, result)))
