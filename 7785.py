#회사에 있는 사람
import sys

input = sys.stdin.readline
N= int(input())
dic ={}
for i in range(N):
    A,B = input().split()
    if B =='enter':
        dic[A] = 1
    else:
        if A in dic:
            del dic[A]
dic2= sorted(dic.keys(), reverse=True)

print('\n'.join(dic2))