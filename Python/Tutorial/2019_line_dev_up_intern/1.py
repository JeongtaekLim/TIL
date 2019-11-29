def run():
    num_msg, max_q_size = map(int, input().strip().split(' '))
    messages = list()
    for i in range(num_msg):
        a = int(input())
        messages.append(a)
    consumers = [None for x in range(max_q_size)]

    cur_time = 0
    while True:
        # 태스크 삭제
        for idx, c in enumerate(consumers):
            if c is None:
                continue
            is_complete = True if cur_time - c['start'] == c['time_cost'] else False
            if is_complete:
                consumers[idx] = None

        # 만약 모든 원소가 None 이면 return
        if all(x is None for x in consumers) and cur_time > 0:
            print(cur_time)
            break

        # 태스크 삽입
        for idx, c in enumerate(consumers):
            # 메시지가 아무것도 없을 때
            if len(messages) == 0:
                continue
            # consumers가 비어있을때 태스크 삽입
            if c is None:
                message = messages[0]
                messages = messages[1:]
                tmp = {'start': cur_time, 'time_cost': message}
                consumers[idx] = tmp
        cur_time += 1


if __name__ == "__main__":
    run()
