def check_words(S, Q):
    S = list(S)
    Q = list(Q)

    for i in range(len(Q)):
        if Q[i] == S[i]:
            S[i] = None
            Q[i] = 'correct'

    for i in range(len(Q)):
        S = get_counter(S)

        if Q[i] in S:
            S[j] = None
            Q[i] = 'present'
            break
        
    for i in range(len(Q)):
        if len(Q[i]) == 1:
            Q[i] = 'absent'
    
    return Q

def get_counter(S):
    pass
    


assert check_words('ABCD', 'AFGD') == ['correct', 'absent', 'absent', 'correct']
assert check_words('CLEVER', 'CREVRS') == ['correct', 'present', 'correct', 'correct', 'absent', 'absent']
assert check_words('ABCD', 'CACD') == ['absent', 'present', 'correct', 'correct']
assert check_words('A', 'C') == ['absent']
assert check_words('A', 'A') == ['correct']
assert check_words('AAAABB', 'BBBBCC') == ['present', 'present', 'absent', 'absent', 'absent', 'absent']




