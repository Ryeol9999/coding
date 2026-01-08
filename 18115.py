#카드 놓기
from collections import deque

N = int(input())
li=list(map(int,input().split()))
#리스트를 거꾸로돌면서
dq = deque()
for i in range(N-1,-1,-1):
    if li[i] == 1:
        dq.appendleft(i)
    elif li[i] == 2 :
        dq.rotate(-1)
        dq.appendleft(i)
        dq.rotate(1)
    elif li[i] == 3:
        dq.append(i)
li= list(dq)
for i in range(N):
    print(N-li[i],end=" ")




