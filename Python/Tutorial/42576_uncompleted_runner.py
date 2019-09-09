def solution(participant, completion):
    participant.sort()
    completion.sort()
    ans = ''
    for idx, c in enumerate(completion):
        if participant[idx] != c:
            ans = participant[idx]
            break
    if ans == '':
        ans = participant[-1]
    return ans


if __name__ == "__main__":
    solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])
