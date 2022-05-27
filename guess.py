with open('input.txt') as input:
    lines = input.read().splitlines()
    S = [i for i in lines[0]]
    Q = [i for i in lines[1]]

for i in range(len(Q)):
    for j in range(len(S)):
        if Q[i] == S[i]:
            S[i] = None
            Q[i] = 'correct'
            break
        elif Q[j] == S[j]:
            S[j] = None
            Q[j] = 'correct'
        elif S[j] == Q[i]:
            S[j] = None
            Q[i] = 'present'
            break
for i in range(len(Q)):
    if len(Q[i]) == 1:
        Q[i] = 'absent'
            

print(S)
print(*Q, sep='\n')
    


# with open('output.txt', 'w') as output:
#     for i in output_list:
#         output.write(i + "\n")