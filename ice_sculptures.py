with open('input.txt', 'r') as input:
    data = input.read().splitlines()
    N = int(data[0].split()[0])
    perfect_weight = int(data[0].split()[1])
    time_left = int(data[0].split()[2])
    weights = list(map(int, data[1].split()))

mapper = dict(zip(range(1, N + 1), [abs(i - perfect_weight) for i in weights]))
mapper = sorted(mapper.items(), key=lambda x: x[1])

ids = []
for id, time in mapper:
    time_left -= time
    if time_left >= 0:
        ids.append(str(id))
    else:
        break

with open('output.txt', 'w') as output:
    if len(ids) == 0:
        output.write('0')
    else:
        output.writelines(str(len(ids)) + '\n')
        output.writelines(' '.join(sorted(ids)))
