from collections import defaultdict

n = int(input())
dct = defaultdict(set)
dct_s = defaultdict(set)


def get_accent_index(s):
    return {i for i, v in enumerate(s) if v.isupper()}


for _ in range(n):
    s = input()
    dct[s.lower()].update(get_accent_index(s))

s = input().split()

ans = 0

for w in s:
    w_set = get_accent_index(w)
    if len(w_set) != 1:
        ans += 1
    elif w.lower() in dct and next(iter(w_set)) not in dct[w.lower()]:
        ans += 1

print(ans)
