line_to_check = 'hellochild'
line_input = 'helto<left><bspace>l<delete>och<right><left>ilds<bspace>'


# line_to_check = input()
# line_input = input()

def print_check(line_to_check, line_input):
    cur_pos = 0
    i = 0
    result = ''
    while i < len(line_input):
        if line_input[i] == '<':
            if line_input[i:i + 6] == '<left>':
                print(line_input[i:i + 6])
                cur_pos = max(0, cur_pos - 1)
                i += 6
                print(result[:cur_pos] + '|' + result[cur_pos:])
            elif line_input[i:i + 7] == '<right>':
                print(line_input[i:i + 7])
                cur_pos = min(cur_pos + 1, len(result))
                i += 7
                print(result[:cur_pos] + '|' + result[cur_pos:])
            elif line_input[i:i + 8] == '<delete>':
                print(line_input[i:i + 8])
                if cur_pos < len(result):
                    result = result[:cur_pos] + result[cur_pos + 1:]
                i += 8
                print(result[:cur_pos] + '|' + result[cur_pos:])

            elif line_input[i:i + 8] == '<bspace>':
                print(line_input[i:i + 8])
                if cur_pos > 0:
                    result = result[:cur_pos - 1] + result[cur_pos:]
                    cur_pos -= 1
                i += 8
                print(result[:cur_pos] + '|' + result[cur_pos:])
        else:
            result = result[:cur_pos] + line_input[i] + result[cur_pos:]
            i += 1
            cur_pos += 1
            print(result[:cur_pos] + '|' + result[cur_pos:])

    return 'No' if result != line_to_check else 'Yes'


print(print_check(line_to_check, line_input))
