n, m = map(int, input().split())

anya, borya = set(), set()
for _ in range(n):
    anya.add(int(input()))

for _ in range(m):
    borya.add(int(input()))

ans = anya.intersection(borya)

print(len(ans))
print(' '.join(map(str, sorted(ans))))
anya_left = anya.difference(ans)
borya_left = borya.difference(ans)
print(len(anya_left))
print(' '.join(map(str, sorted(anya_left))))
print(len(borya_left))
print(' '.join(map(str, sorted(borya_left))))
