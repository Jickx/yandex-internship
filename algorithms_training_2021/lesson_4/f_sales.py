import sys
from collections import defaultdict

data = sys.stdin.read().splitlines()

sales_table = defaultdict(lambda: defaultdict(int))
for i in data:
    lastname, product, qty = i.split()
    sales_table[lastname][product] += int(qty)

for lastname, product in sorted(sales_table.items()):
    print(f'{lastname}:')
    for product_name, qty in sorted(product.items()):
        print(f'{product_name} {qty}')
