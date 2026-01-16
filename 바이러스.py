import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def bfs(start):
    global count
    queue = deque([start])
    visited[start] = True

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)


bfs(1)
print(count)

