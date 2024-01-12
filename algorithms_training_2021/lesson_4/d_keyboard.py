n = int(input())
c = [None] + list(map(int, input().split()))

k = input()
p = list(map(int, input().split()))

keys = {k: 0 for k in range(1, n + 1)}
result = []
for i in p:
    keys[i] += 1

for i in range(1, n + 1):
    if keys[i] > c[i]:
        result.append('YES')
    else:
        result.append('NO')

print(' '.join(result))
