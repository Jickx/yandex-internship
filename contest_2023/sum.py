with open('input.txt') as input:
    content = input.read()
    a, b = content.split()

with open('output.txt', 'w') as output:
    total = int(a) + int(b)
    output.write(str(total))

