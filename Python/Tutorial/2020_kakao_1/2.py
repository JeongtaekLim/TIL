def solution(p):
    # mystr은 1이상이라는 전제
    def get_reversed(my_str):
        result = ""
        for s in my_str:
            if s == ")":
                result += "("
            else:
                result += ")"
        return result

    def is_right(my_str):
        my_stack = []
        for s in my_str:
            if s == "(":
                my_stack.append(s)
            else:
                if len(my_stack) == 0 or my_stack[-1] != "(":
                    return False
                my_stack = my_stack[:-1]
        return True

    def get_u_v(my_str):
        cnt = [0, 0]
        for idx, s in enumerate(my_str):
            if s == "(":
                cnt[0] += 1
            else:
                cnt[1] += 1
            if cnt[0] > 0 and cnt[1] > 0 and cnt[0] == cnt[1]:
                return my_str[:idx + 1], my_str[idx + 1:]

    def fix_func(my_str):
        if len(my_str) == 0:  # 1번조건
            return ""
        u, v = get_u_v(my_str)  # 2번조건
        if is_right(u):
            return u + fix_func(v)  # 3번, 3-1번 조건
        else:
            tmp = "("  # 4 -1번조건
            tmp += fix_func(v)  # 4-2번조건
            tmp += ")"  # 4-3번조건
            u = u[1:-1]  # 4-4 번조건
            u = get_reversed(u)  # 4-4 번조건
            return tmp + u

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    # 4-3. ')'를 다시 붙입니다.
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    # 4-5. 생성된 문자열을 반환합니다.
    answer = fix_func(p)
    return answer


if __name__ == "__main__":
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))