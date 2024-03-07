n = int(input())
seq = []
for i in range(n):
    seq.append(int(input()))


def binary_sequence(seq):
    max_seq = 0
    curr_seq = 0
    for i in seq:
        if i == 1:
            curr_seq += 1
        else:
            max_seq = max(max_seq, curr_seq)
            curr_seq = 0
    max_seq = max(max_seq, curr_seq)
    return max_seq


print(binary_sequence(seq))
