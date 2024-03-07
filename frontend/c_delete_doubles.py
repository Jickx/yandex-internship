with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    n = int(input_file.readline())
    prev = None
    for _ in range(n):
        line = input_file.readline().strip('\n')
        if prev != line:
            output_file.write(line + '\n')
            prev = line
