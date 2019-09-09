def solution(s):
    def get_compress_str(_s, k):  # k는 단어의 길이
        result = ''
        cnt = 0
        tmp = ''
        while True:
            # 최초 접근시
            if len(tmp) == 0:
                tmp = _s[:k]
                cnt = 1
                _s = _s[k:]  # s 절삭
                continue
            # 단어 하나를 찾은 이후 접근
            if len(tmp) > 0:
                if tmp == _s[:k]:
                    cnt += 1
                    _s = _s[k:]  # s 절삭
                    continue
            result = result + str(cnt) + tmp if cnt > 1 else result + tmp
            cnt = 0
            tmp = ''
            if len(_s) < k:
                result = result + _s
                break
        return result, len(result)
    answer = 999999
    for length in range(1, 1 + len(s)):
        r, a = get_compress_str(s, length)
        if a < answer:
            answer = a
    return answer


if __name__ == "__main__":
    print(solution("a"))
    print(solution("aa"))
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
