#터렛
from math import sqrt

N = int(input())
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        X = (x1 - x2)
        Y = (y1 - y2)
        length = sqrt(X**2 + Y**2)
        min = abs(r1 - r2)
        max = abs(r1 + r2)
        if length == min or length == max:
            print(1)
        elif length > min and length < max:
            print(2)
        else:
            print(0)

