n = int(input())
print(len({input().split()[0] for _ in range(n)}))