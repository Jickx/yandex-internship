n = int(input())
lst = []
turtles = {tuple(map(int, input().split())) for _ in range(n)}
turtles_sum = list(map(sum, turtles))

result = {}
for i in turtles_sum:
    result[i] = result.get(i, 0) + 1

print(max(result.values()))
