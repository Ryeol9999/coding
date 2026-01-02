# https://www.acmicpc.net/problem/1037
# 백준 1037번문제 약수
N= int(input())
li =list(map(int,input().split()))

li.sort()
if len(li)==1:
    print(li[0]*li[0])
else:
    print(li[0]*li[len(li)-1])