from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 여기서 정렬을 한 번 해줘야겠죠?
for i in range(1, N + 1):
    graph[i].sort()
dq=deque()
for i in range(gr
