def run():
    n = int(input())
    seats = [int(x) for x in input().strip().split(' ')]
    max_idx, max_len, tmp_idx, tmp_len = None, 0, None, 0

    for idx, s in enumerate(seats):
        if s == 0:
            if tmp_idx is None:
                tmp_idx = idx
                tmp_len = 1
            else:
                tmp_len += 1
        else:
            if max_len < tmp_len:
                max_idx, max_len = tmp_idx, tmp_len
            tmp_idx, tmp_len = None, 0
    if max_idx is None:
        max_idx, max_len = tmp_idx, tmp_len

    # 찾아낸 연속 0 그룹이 seats의 맨 처음에 있거나 맨 끝에 있을 경우
    if max_idx == 0 or max_idx + max_len == len(seats):
        ans = max_len
    else:
        ans = int((max_len + 1) / 2)
    print(ans)


if __name__ == "__main__":
    run()
