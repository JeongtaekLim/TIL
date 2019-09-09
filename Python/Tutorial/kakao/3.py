def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    full_map = [[]]
    my_key = key
    my_lock = lock

    def reset_full_map():
        result = [[0 for i in range(n + 2 * m)] for j in range(n + 2 * m)]
        return result

    def draw_lock():
        for row_idx, row in enumerate(my_lock):
            for col_idx, v in enumerate(row):
                full_map[row_idx + m][col_idx + m] = v

    def draw_key(x, y):
        for row_idx, row in enumerate(my_key):
            for col_idx, v in enumerate(row):
                full_map[x + row_idx][y + col_idx] += v

    def is_unlocked():
        for i in range(m, m + n):
            for j in range(m, m + n):
                if full_map[i][j] != 1:
                    return False
        return True

    def show_full_map():
        for row in full_map:
            for v in row:
                print("{} ".format(v), end="")
            print("")

    def get_rotated_key():
        return list(zip(*reversed(my_key)))

    for k in range(4):
        if k > 0:
            my_key = get_rotated_key()
        for i in range(n + m):
            for j in range(n + m):
                full_map = reset_full_map()
                draw_lock()
                draw_key(i, j)
                # show_full_map()
                if is_unlocked():
                    answer = True
    return answer


if __name__ == "__main__":
    # print(1)
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
