#포켓몬 마스터 이다솜

N, M = map(int, input().split())
dic = {}
for i in range(1,N+1):
    name = input()
    dic[str(i)] = name
for i in range(M):
    NN = input()
    if NN in dic:
        print(dic[NN])
    else :
        print(dic.values(NN))
