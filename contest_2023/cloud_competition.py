with open('input.txt', 'r') as f:
    data = []
    for line in f.readlines():
        data.append(line.strip('\n'))

competition_parameters = {}
competitors_results = []
number_of_finals = int(data[0])
number_of_competitors = int(data[number_of_finals + 1])

for i in range(1, number_of_finals + 1):
    line = tuple(data[i].split(','))
    competition_parameters[line[0]] = int(line[1])

for i in range(
        number_of_finals + 2,
        number_of_finals + 2 + number_of_competitors):
    line = tuple(data[i].split(','))
    competitor_result = {
        'name': line[0],
        'competition': line[1],
        'scores': line[2],
        'penalty': line[3]
    }
    competitors_results.append(competitor_result.copy())
    competitor_result.clear()


def get_finalists(
        _competition_parameters,
        _competitors_results):
    print(_competition_parameters, _competitors_results)


get_finalists(competition_parameters, competitors_results)


# with open('output.txt', 'w') as output:
#     output.write(str(check_plagiarism(alice, zeliboba)))
