n = int(input())
result = set()
for _ in range(n):
    a, b = map(int, input().split())
    if a + b == n - 1 and (a, b) not in result:
        result.add((a, b))

print(len(result))
