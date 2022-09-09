from collections import Counter


def check_plagiarism(alice, zeliboba) -> str:
    alice, zeliboba = list(alice), list(zeliboba)
    alice_ctr = dict(Counter(alice))
    result = [None for i in range(len(alice))]
    i = 0
    while i < len(alice):
        if zeliboba[i] == alice[i]:
            alice_ctr[alice[i]] -= 1
            alice[i], zeliboba[i] = None, None
            result[i] = 'P'
            i += 1
            continue
        i += 1
    for i in range(len(zeliboba)):
        if not zeliboba[i]:
            continue
        if zeliboba[i] in alice_ctr and alice_ctr[zeliboba[i]] > 0:
            alice_ctr[zeliboba[i]] -= 1
            zeliboba[i] = None
            result[i] = 'S'
        else:
            result[i] = 'I'
    return ''.join(result)


# with open('input.txt') as input:
#     lines = input.read().splitlines()
#     alice = lines[0]
#     zeliboba = lines[1]
#
# with open('output.txt', 'w') as output:
#     output.write(str(check_plagiarism(alice, zeliboba)))


assert check_plagiarism('CLOUD', 'CUPID') == 'PSIIP'
assert check_plagiarism('ALICE', 'ELIBO') == 'SPPII'
assert check_plagiarism('ABCBCYA', 'ZBBACAA') == 'IPSSPIP'
