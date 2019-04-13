# coding: utf-8
def seventh(data):
    data.sort()
    # constant data
    chord_set = [{0, 4, 7, 10}, {0, 4, 7, 11}, {0, 3, 7, 10}, {0, 3, 7, 11},
                 {0, 3, 6, 10}, {0, 3, 6, 9}, {0, 4, 8, 11}, {0, 5, 7, 10},
                 {0, 4, 7, 9}, {0, 3, 7, 9}, {0, 2, 4, 7}, {0, 4, 5, 7},
                 {0, 4, 6, 10}, {0, 4, 8, 10}]
    chord_name = {0: '7', 1: 'M7', 2: 'm7', 3: 'mM7', 4: 'm7-5', 5: 'dim7', 6: 'M7+5', 7: '7sus4',
                  8: '6', 9: 'm6', 10: '(add9)', 11: '(add4)', 12: '7-5', 13: 'aug7', -1: ''}
    root_name = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab',
                 9: 'A', 10: 'Bb', 11: 'B', -1: ''}
    # input,necessary elements
    chord_name_value = -1
    root_name_value = -1
    trans_value = min(data)
    transposed = [data[0]-trans_value, data[1]-trans_value, data[2]-trans_value, data[3]-trans_value]
    tb_a = [(transposed[0] - transposed[1]) % 12, 0,
            (transposed[2] - transposed[1]) % 12, (transposed[3] - transposed[1]) % 12]
    tb_b = [(transposed[0] - transposed[2]) % 12, (transposed[1] - transposed[2]) % 12,
            0, (transposed[3] - transposed[2]) % 12]
    tb_c = [(transposed[0] - transposed[3]) % 12, (transposed[1] - transposed[3]) % 12,
            (transposed[2] - transposed[3]) % 12, 0]
    # search(transposed)
    for i in range(14):
        if set(transposed) == chord_set[i]:
            chord_name_value = i
            root_name_value = trans_value
            break
    else:
        # search(tb_a)
        for j in range(14):
            if set(tb_a) == chord_set[j]:
                chord_name_value = j
                root_name_value = trans_value + transposed[1]
                break
        else:
            # search(tb_b)
            for k in range(14):
                if set(tb_b) == chord_set[k]:
                    chord_name_value = k
                    root_name_value = trans_value + transposed[2]
                    break
            else:
                # search(tb_c)
                for l in range(14):
                    if set(tb_c) == chord_set[l]:
                        chord_name_value = l
                        root_name_value = trans_value + transposed[3]
                        break

    ans = "{}{}".format(root_name[root_name_value], chord_name[chord_name_value])
    if root_name_value == -1 and chord_name_value == -1:
        ans = 'No results'

    return ans
