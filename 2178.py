#미로 탐색
from collections import deque

N , M = map(int, input().split())


array = [list(input()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

# print(array)
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if 0 <= x2 <= N - 1 and  0 <= y2 <= M - 1:
                if visited[x2][y2] == 0 and array[x2][y2] == '1':
                    visited[x2][y2] = visited[x][y] + 1
                    queue.append((x2,y2))

    return visited[N-1][M-1]

print(bfs(0,0))