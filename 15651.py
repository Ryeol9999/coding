#N과 M (3)

from itertools import permutations, product

N, M = map(int, input().split())
for i in product([i for i in range(1,N+1)] for j in range(1,M+1)):
    print(*i)