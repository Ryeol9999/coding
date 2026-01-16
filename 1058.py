# 친구
import sys

input = sys.stdin.readline
N = int(input())

Gp = [ [input()] for _ in range(N)]
print(Gp)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if Gp[i][k] == 'Y' and Gp[k][j] == 'Y':
                Gp[k][j] = 'Y'
MAX = 0
for i in range(N):
    count = 0
    for j in range(N):
        if Gp[i][j] == 'Y':
            count += 1
    if count >= MAX:
        MAX = count
print(MAX)