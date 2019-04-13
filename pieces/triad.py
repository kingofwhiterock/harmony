# coding: utf-8
def triad(data):
    data.sort()
    # constant data
    chord_set = [{0, 4, 7}, {0, 3, 7}, {0, 3, 6}, {0, 4, 8}, {0, 5, 7}, {0, 4, 6}]
    chord_name = {0: '', 1: 'm', 2: 'dim', 3: 'aug', 4: 'sus4', 5: '-5', -1: ''}
    root_name = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab',
                 9: 'A', 10: 'Bb', 11: 'B', -1: ''}
    # input,necessary elements
    chord_name_value = -1
    root_name_value = -1
    trans_value = min(data)
    transposed = [data[0]-trans_value, data[1]-trans_value, data[2]-trans_value]
    tb_a = [(transposed[0] - transposed[1]) % 12, 0, (transposed[2] - transposed[1]) % 12]
    tb_b = [(transposed[0] - transposed[2]) % 12, (transposed[1] - transposed[2]) % 12, 0]
    # search(transposed)
    for i in range(6):
        if set(transposed) == chord_set[i]:
            chord_name_value = i
            root_name_value = trans_value
            break
    else:
        # search(tb_a)
        for j in range(6):
            if set(tb_a) == chord_set[j]:
                chord_name_value = j
                root_name_value = trans_value + transposed[1]
                break
        else:
            # search(tb_b)
            for k in range(6):
                if set(tb_b) == chord_set[k]:
                    chord_name_value = k
                    root_name_value = trans_value + transposed[2]
                    break

    ans = "{}{}".format(root_name[root_name_value], chord_name[chord_name_value])
    if root_name_value == -1 and chord_name_value == -1:
        ans = 'No results'

    return ans
