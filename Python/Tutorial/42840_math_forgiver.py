from functools import cmp_to_key


def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [[0, 0], [1, 0], [2, 0]]
    for ans_idx, ans in enumerate(answers):
        for p_idx, p in enumerate(pattern):
            if p[ans_idx % len(p)] == ans:
                score[p_idx][1] += 1
    score = sorted(score, key=cmp_to_key(lambda x, y: y[1] - x[1]))
    answer = []
    for idx, s in enumerate(score):
        if len(answer) == 0:
            answer.append(s[0]+1)
            continue
        if score[idx-1][1] == s[1]:
            answer.append(s[0]+1)
        else:
            break
    answer.sort()
    return answer


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5])
    solution([1, 3, 2, 4, 2])
