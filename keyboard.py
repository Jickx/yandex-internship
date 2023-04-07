with open('input.txt') as input:
    data = input.read()
    data_list = data.split('\n')
    keys_qty = data_list[0]
    keys_id_lst = list(map(int, data_list[1].split()))
    row = list(map(int, data_list[2].split()))
    keys_id_dict = dict(zip(keys_id_lst, row))
    symb_qty = data_list[3]
    symb_flow = list(map(int, data_list[4].split()))

changed_row = False
ctr = 0
prev_row = keys_id_dict[symb_flow[0]]
for i in range(len(symb_flow)):
    cur_row = keys_id_dict[symb_flow[i]]
    if cur_row != prev_row:
        ctr += 1
        prev_row = cur_row

with open('output.txt', 'w') as output:
    output.write(str(ctr))




