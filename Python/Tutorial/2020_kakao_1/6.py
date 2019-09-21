import itertools


def solution(n, weak, dist):
    WEAK_POINT = -1
    wall = [0 in range(n)]
    for w in weak:
        wall[w] = WEAK_POINT
    def is_fixible(tmp_wall, start_point, friend):
        # 양의 방양으로 갈 때,
        return False
    for i in range(1, 1 + len(dist)):
        # i명의 친구들 선정
        friends = list(itertools.combinations(dist, i))
        # i개의 출발 취약지점 선정
        weak_points = list(itertools.combinations(weak, i))
        for friend in friends:
            # friend의 조합 선정
            permu_friend = list(itertools.permutations(friend))
            for idx, friend in enumerate(permu_friend):
                pass



    answer = 0
    return answer


if __name__ == "__main__":
    solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
