if __name__ == "__main__":
    # relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
    #             ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
    relation = [
        [1, 1],
        [2, 3],
    ]
    comb_tmp = []
    comb_src = []
    col_combs = []
    ans = []

    def is_unique(_col_comb):
        values = []
        for r in relation:
            tmp = []
            for col in _col_comb:
                tmp.append(r[col])
            if tmp in values:
                tmp.sort()
                return False
            values.append(tmp)
        return True


    def is_minimal(tmp):
        for a in ans:
            if len(list(filter(lambda x: x in tmp, a))) == len(a):
                return False
        return True


    num_rows = len(relation)
    num_cols = len(relation[0])
    # column index의 조합 setting
    comb_src = range(num_cols)


    def comb(start, num):
        global comb_tmp
        end = len(comb_src)
        if num == 0:
            col_combs.append(comb_tmp)
            return
        for i in range(start, end):
            comb_tmp.append(comb_src[i])
            comb(i + 1, num - 1)
            comb_tmp = comb_tmp[:-1]


    for i in range(1, num_cols + 1):
        comb(0, i)
    for col_comb in col_combs:
        if is_minimal(col_comb) and is_unique(col_comb):
            ans.append(col_comb)
    print(len(ans))
    print(ans)
