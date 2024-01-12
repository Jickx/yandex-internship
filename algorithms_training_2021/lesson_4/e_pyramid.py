from collections import defaultdict

n = int(input())

d = defaultdict(list)
for _ in range(n):
    w, h = map(int, input().split())
    d[w].append(h)

result = 0
for v in d.values():
    result += max(v)

print(result)
