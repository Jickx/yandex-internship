from collections import defaultdict


def is_anagram(t: str, s: str) -> bool:
    dct = defaultdict(int)
    for i in t:
        dct[i] += 1
    dct2 = defaultdict(int)
    for i in s:
        dct2[i] += 1
    return dct == dct2


print(is_anagram('anagram', 'marnaga'))
