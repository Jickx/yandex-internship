from collections import Counter

n, m = map(int, input().split())
w = Counter(input())
s = input()


start = 0
end = n
ctr = 0

while end < len(s) + 1:
    if Counter(s[start:end]) == w:
        ctr += 1
    start += 1
    end += 1
print(ctr)
