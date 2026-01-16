#치킨배달

N, M = map(int, input().split())
arr= []
for i in range(N):
    arr.append(list(map(int, input().split())))
visited =[[False]*N for _ in range(N)]
print(visited)
chicken= []
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            chicken.append([i,j])
def dfs