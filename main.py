# coding: utf-8
class HarmonyDetect:
    def __init__(self, data1):
        self.root_name = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab',
                          9: 'A', 10: 'Bb', 11: 'B', -1: ''}
        self.data = data1

    def triad(self):
        self.data.sort()
        # constant data
        chord_set = [{0, 4, 7}, {0, 3, 7}, {0, 3, 6}, {0, 4, 8}, {0, 5, 7}, {0, 4, 6}]
        chord_name = {0: '', 1: 'm', 2: 'dim', 3: 'aug', 4: 'sus4', 5: '-5', -1: ''}
        # input,necessary elements
        chord_name_value = -1
        root_name_value = -1
        trans_value = min(self.data)
        transposed = [self.data[0]-trans_value, self.data[1]-trans_value, self.data[2]-trans_value]
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

        ans = "{}{}".format(self.root_name[root_name_value], chord_name[chord_name_value])
        if root_name_value == -1 and chord_name_value == -1:
            ans = 'No results'

        return ans

    def seventh(self):
        self.data.sort()
        # constant data
        chord_set = [{0, 4, 7, 10}, {0, 4, 7, 11}, {0, 3, 7, 10}, {0, 3, 7, 11},
                     {0, 3, 6, 10}, {0, 3, 6, 9}, {0, 4, 8, 11}, {0, 5, 7, 10},
                     {0, 4, 7, 9}, {0, 3, 7, 9}, {0, 2, 4, 7}, {0, 4, 5, 7},
                     {0, 4, 6, 10}, {0, 4, 8, 10}]
        chord_name = {0: '7', 1: 'M7', 2: 'm7', 3: 'mM7', 4: 'm7-5', 5: 'dim7', 6: 'M7+5', 7: '7sus4',
                      8: '6', 9: 'm6', 10: '(add9)', 11: '(add4)', 12: '7-5', 13: 'aug7', -1: ''}
        # input,necessary elements
        chord_name_value = -1
        root_name_value = -1
        trans_value = min(self.data)
        transposed = [self.data[0]-trans_value, self.data[1]-trans_value,
                      self.data[2]-trans_value, self.data[3]-trans_value]
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

        ans = "{}{}".format(self.root_name[root_name_value], chord_name[chord_name_value])
        if root_name_value == -1 and chord_name_value == -1:
            ans = 'No results'

        return ans

    def ninth(self):
        self.data.sort()
        # constant data
        chord_set = [{0, 2, 4, 7, 10}, {0, 1, 4, 7, 10}, {0, 3, 4, 7, 10}, {0, 4, 5, 7, 10}, {0, 3, 5, 7, 10},
                     {0, 4, 6, 7, 10}, {0, 4, 6, 7, 11}, {0, 4, 7, 9, 10}, {0, 4, 7, 8, 10}, {0, 2, 4, 7, 9},
                     {0, 2, 3, 7, 9}]
        chord_name = {0: '9', 1: '7(b9)', 2: '7(b10)', 3: '7(11)', 4: 'm7(11)', 5: '7(#11)', 6: 'M7(#11)', 7: '7(13)',
                      8: '7(b13)', 9: '69', 10: 'm69', -1: ''}
        # input, necessary data
        chord_name_value = -1
        root_name_value = -1
        trans_value = min(self.data)
        transposed = [self.data[0]-trans_value, self.data[1]-trans_value, self.data[2]-trans_value,
                      self.data[3]-trans_value, self.data[4]-trans_value]
        tb_a = [(transposed[0] - transposed[1]) % 12, 0, (transposed[2] - transposed[1]) % 12,
                (transposed[3] - transposed[1]) % 12, (transposed[4] - transposed[1]) % 12]
        tb_b = [(transposed[0] - transposed[2]) % 12, (transposed[1] - transposed[2]) % 12,
                0, (transposed[3] - transposed[2]) % 12, (transposed[4] - transposed[2]) % 12]
        tb_c = [(transposed[0] - transposed[3]) % 12, (transposed[1] - transposed[3]) % 12,
                (transposed[2] - transposed[3]) % 12, 0, (transposed[4] - transposed[3]) % 12]
        tb_d = [(transposed[0] - transposed[4]) % 12, (transposed[1] - transposed[4]) % 12,
                (transposed[2] - transposed[4]) % 12, (transposed[3] - transposed[4]) % 12, 0]
        # search(transposed)
        for i in range(11):
            if set(transposed) == chord_set[i]:
                chord_name_value = i
                root_name_value = trans_value
                break
        else:
            # search(tb_a)
            for j in range(11):
                if set(tb_a) == chord_set[j]:
                    chord_name_value = j
                    root_name_value = trans_value + transposed[1]
                    break
            else:
                # search(tb_b)
                for k in range(11):
                    if set(tb_b) == chord_set[k]:
                        chord_name_value = k
                        root_name_value = trans_value + transposed[2]
                        break
                else:
                    # search(tb_c)
                    for l in range(11):
                        if set(tb_c) == chord_set[l]:
                            chord_name_value = l
                            root_name_value = trans_value + transposed[3]
                            break
                    else:
                        # search(tb_d)
                        for m in range(11):
                            if set(tb_d) == chord_set[m]:
                                chord_name_value = m
                                root_name_value = trans_value + transposed[4]
                                break

        ans = "{}{}".format(self.root_name[root_name_value], chord_name[chord_name_value])
        if root_name_value == -1 and chord_name_value == -1:
            ans = 'No results'

        return ans


def main():
    r_data = list(map(int, input().split()))
    hd = HarmonyDetect(r_data)
    if len(r_data) < 3:
        print('No results')
    elif len(r_data) == 3:
        print(hd.triad())
    elif len(r_data) == 4:
        print(hd.seventh())
    elif len(r_data) == 5:
        print(hd.ninth())
    else:
        print('No results')


if __name__ == '__main__':
    main()
