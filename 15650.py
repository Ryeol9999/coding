#N과 M (2)
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs():
    if len(li) == M:
        print(*li)
        return

    for i in range (1, N+1):
        if len(li) == 0:
            li.append(i)
            dfs()
            li.pop()
        else:
            if li[len(li)-1] < i:
                li.append(i)
                dfs()
                li.pop()
N, M= map(int, input().split())
li = [ ]
dfs()