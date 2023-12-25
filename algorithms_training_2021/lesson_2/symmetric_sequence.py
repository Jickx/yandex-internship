def make_palindrome(arr: list[int]) -> str:
    s = ''.join(map(str, arr))
    for i in range(len(s)):
        if (s + s[:i][::-1]) == (s + s[:i][::-1])[::-1]:
            return s[:i][::-1]


n = input()
result = make_palindrome(list(map(int, input().split())))
if result:
    print(len(result))
    print(' '.join(list(result)))
else:
    print('0')
