def run():
    lookup = [[None for col in range(25)] for row in range(25)]

    for row_idx, row in enumerate(lookup):
        for col_idx, v in enumerate(row):
            if row_idx == 0 and col_idx == 0:
                lookup[row_idx][col_idx] = 0
                continue
            elif row_idx == 0:
                lookup[row_idx][col_idx] = 1
                continue
            elif col_idx == 0:
                lookup[row_idx][col_idx] = 1
                continue
            lookup[row_idx][col_idx] = lookup[row_idx - 1][col_idx] + lookup[row_idx][col_idx - 1]

    n, m = map(int, input().strip().split(' '))
    con_n, con_m = map(int, input().strip().split(' '))
    if con_n > n or con_m > m:
        print("fail")
        return
    print(con_n + con_m)
    print(lookup[con_n][con_m])


if __name__ == "__main__":
    run()
