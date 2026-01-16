import queue
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
visted = []
for i in range(H):
    array = []
    for j in range(N):
        array.append(list(map(int, input().split())))
    graph.append(array)
# print(graph)
dq = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                dq.append((i, j, k))



def bfs(X):
    queue = X
    count = len(queue) # queue 길의
    count2 = 0
    count3 =0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dz = [-1, 1]

    while queue:
        z, x, y = queue.popleft()
        count2 += 1
        for i in range(2):
            z2 = z + dz[i]
            if 0 <= z2 <= H - 1  and graph[z2][x][y] == 0:
                graph[z2][x][y] = 1
                queue.append((z2, x, y))
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if 0 <= x2 <= N - 1 and 0 <= y2 <= M - 1 and graph[z][x2][y2] == 0:
                graph[z][x2][y2] = 1
                queue.append((z, x2, y2))
        if count2 == count :
            count3 += 1
            count2 = 0
            count = len(queue)
    return count3
count4 = 0
answer = bfs(dq)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                count4 += 1
if count4 == 0:
    print(answer - 1)
else:
    print(-1)




