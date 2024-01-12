import sys

s = sys.stdin.read().split()

max_count = 0
common_words_set = set()
dct = {}

for word in s:
    dct[word] = dct.get(word, 0) + 1
    if dct[word] > max_count:
        max_count = dct[word]
        common_words_set.clear()
        common_words_set.add(word)
    if dct[word] == max_count:
        common_words_set.add(word)

print(min(common_words_set))
