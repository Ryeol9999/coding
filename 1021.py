#회전하는 큐
from collections import deque

N,M =map(int,input().split())
li = list(map(int,input().split()))

dq =deque()
count = 0
for i in range(1,N+1):
    dq.append(i)
for i in range(M):
        index = dq.index(li[i])
        if index > len(dq)//2:
            for _ in range(len(dq)-index):
                X = dq.pop()
                dq.appendleft(X)
                count +=1
        else:
            for _ in range(index):
                X = dq.popleft()
                dq.append(X)
                count +=1
        dq.popleft()
print(count)
