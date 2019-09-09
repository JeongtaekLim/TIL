def solution(n, computers):
    visited = []

    def bfs(start):
        q = []
        q.append(start)
        while len(q) > 0:
            cur = q[0]
            q = q[1:]
            visited.append(cur)
            for idx, c in enumerate(computers[cur]):
                if idx not in visited and c == 1:
                    q.append(idx)

    cnt = 0
    for i in range(n):
        if i not in visited:
            bfs(i)
            cnt += 1
    return cnt


if __name__ == "__main__":
    solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
