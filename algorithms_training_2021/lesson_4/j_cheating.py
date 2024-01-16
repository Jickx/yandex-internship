import re
import sys
from collections import defaultdict

bools = {'yes': True, 'no': False}

n, is_case_sensitive, is_first_num = input().split()

keywords = [input() for _ in range(int(n))]

data = sys.stdin.read()

ids = re.findall(r'(?=.*[a-zA-Z_])[a-zA-Z0-9_]+', data)

if not bools[is_first_num]:
    ids = [i for i in ids if not i[0].isdigit()]

if not bools[is_case_sensitive]:
    ids = [i.lower() for i in ids]
    keywords = [i.lower() for i in keywords]

if len(keywords) > 0:
    ids = [i for i in ids if i not in keywords]

ids_dct = defaultdict(int)
for i in ids:
    ids_dct[i] += 1

print(max(ids_dct, key=lambda x: ids_dct.get(x, 0)))
