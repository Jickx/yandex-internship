def check_plagiarism(alice, zeliboba):
    alice = list(alice)
    zeliboba = list(zeliboba)
    result = [None for i in range(len(alice))]
    i = 0
    while i < len(alice):
        if zeliboba[i] == alice[i]:
            alice[i], zeliboba[i] = None, None
            result[i] = 'P'
            i += 1
            continue
        i += 1
    i = 0
    while i < len(alice):
        if not zeliboba[i]:
            i += 1
            continue
        if zeliboba[i] in alice:
            letter_index = alice.index(zeliboba[i])
            alice[letter_index] = None
            zeliboba[i] = None
            result[i] = 'S'
        else:
            result[i] = 'I'
            zeliboba[i] = None
        i += 1
    return ''.join(result)


# with open('input.txt') as input:
#     lines = input.read().splitlines()
#     alice = lines[0]
#     zeliboba = lines[1]
#
# with open('output.txt', 'w') as output:
#     output.write(str(check_plagiarism(alice, zeliboba)))


assert check_plagiarism('CLOUD', 'CUPID') == 'PSIIP'
# assert check_plagiarism('ALICE', 'ELIBO') == 'SPPII'
# assert check_plagiarism('ABCBCYA', 'ZBBACAA') == 'IPSSPIP'
