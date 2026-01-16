from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# [입력 부분] - 방금 작성하신 것
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# [장부와 카운트]
visited = [False] * (N + 1)
count = 0


# [BFS 청소기 정의]
def bfs(start):
    queue = deque([start])
    visited[start] = True  # 줄 세우자마자 장부에 체크!

    while queue:
        curr = queue.popleft()  # 줄 맨 앞사람 나와!
        print(queue)
        for neighbor in graph[curr]:  # 그 사람 친구들 다 모여!
            if not visited[neighbor]:  # 처음 보는 친구면?
                visited[neighbor] = True  # 장부 체크하고
                queue.append(neighbor)  # 줄 세우기!


# [전체 마을 순회]
for i in range(1, N + 1):
    if not visited[i]:  # 아직 청소 안 된 섬을 발견하면?
        bfs(i)  # BFS 청소기 가동!
        count += 1  # 섬 개수 +1

print(count)