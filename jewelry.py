with open('input.txt') as input:
    lines = input.read().splitlines()
    jewelery = lines[0]
    stones = lines[1]
    
count = 0

for stone in stones:
    if stone in jewelery:
        count += 1

with open('output.txt', 'w') as output:
    output.write(str(count))
