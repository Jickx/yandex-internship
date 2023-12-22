def rle(s: str) -> str:
    ans = []
    last = s[0]
    ctr = 1
    for i in range(1, len(s)):
        if last == s[i]:
            ctr += 1
        else:
            ans.append(last)
            last = s[i]
            if ctr > 1:
                ans.append(str(ctr))
            ctr = 1
    ans.append(last)
    if ctr > 1:
        ans.append(str(ctr))
    return ''.join(ans)


print(rle('AAABBBBCCCCCDDE'))
