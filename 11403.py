# 경로 찾기

N = int(input())
Gp=[]
for i in range(N):
    Gp.append(list(map(int, input().split())))
for k in range(N):
    for i in range (N):
        for j in range (N):
            if Gp[i][k] == 1 and Gp[k][j] == 1:
                Gp[i][j]=1
for row in Gp:
    print(*row)