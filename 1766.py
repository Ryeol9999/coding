from collections import deque

N, K = map(int, input().split())
dq= deque()
for i in range(N):
    dq.append(i+1)
print(dq)