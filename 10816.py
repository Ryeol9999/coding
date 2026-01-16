#숫자 카드 2

N= int(input())
li = list(map(int,input().split()))

M= int(input())
li2= list(map(int,input().split()))

dic = {}
for i in range(N):
    if li[i] not in dic:
        dic[li[i]] = 1
    else:
        dic[li[i]] += 1
for i in range(M):
    print(dic.get(li2[i],0), end=' ')


