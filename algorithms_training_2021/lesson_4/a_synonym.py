n = int(input())

dct = {}
for _ in range(n):
    k, v = input().split()
    dct[k] = v
    dct[v] = k

print(dct[input()])
