#안전 영역
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y,k):
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] > k:
            dfs(nx, ny, k)

N = int(input())
arr = []
Max = 0
for _ in range(N):
    X =list(map(int, input().split()))
    if max(X) > Max:
        Max = max(X)
    arr.append(X)
# print(Max)
max_count = 0
for k in range(Max):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and visited[i][j] == False:
                dfs(i, j, k)
                count += 1
    if count > max_count:
        max_count = count
print(max_count)
