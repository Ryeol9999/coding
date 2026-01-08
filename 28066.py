#타노스는 요세푸스가 밉다
from collections import deque

N, K = map(int, input().split())
dq = deque()
for i in range(1,N+1):
    dq.append(i)
while len(dq)>K:
    for i in range(K):
        if i == 0:
            X = dq.popleft()
            dq.append(X)
        else:
            X = dq.popleft()
print(dq.popleft())