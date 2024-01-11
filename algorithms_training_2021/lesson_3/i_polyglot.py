n = int(input())
pupils_langs = []
langs_set = set()
for _ in range(n):
    m = int(input())
    lang = set()
    for _ in range(m):
        lang.add(input().strip('\n'))
    langs_set.update(lang)
    pupils_langs.append(lang)

know_everybody = set()
for i in langs_set:
    is_know = True
    for j in pupils_langs:
        if i not in j:
            is_know = False
    if is_know:
        know_everybody.add(i)

print(len(know_everybody))
for i in know_everybody:
    print(i)
print(len(langs_set))
for i in langs_set:
    print(i)
