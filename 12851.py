#숨박꼭질 2
from collections import deque

N, K = map(int, input().split())


#  +1, -1 , *2는 한번
visted = [0] * 100001
dq = deque()
dq.append(0)
def bfs(start, end):
    dq = deque()
    dq.append(start)
    count = 0
    number = 0
    visted[start] = 1
    while dq:
        count += 1
        for _ in range(len(dq)): # 노드의 길이만큼 반복
            node = dq.popleft() # 노드를 꺼내옴
            li = []
            li.append(node+1) # +1
            li.append(node-1) # -1
            li.append(node*2) # *2
            for x in li:
                if x == end:
                    number += 1
                elif 0<= x <= 100000:
                    if visted[x] == 0 or visted[x] == count:
                        dq.append(x)
                        visted[x] = count

        if number != 0:
            return count, number
if N == K:
    print(0)
    print(1)
else:
    count, number = bfs(N, K)
    print(count)
    print(number)
