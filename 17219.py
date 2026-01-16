#비밀번호 찾기

N, M = map(int, input().split())
dic = {}
for i in range(N):
    A, B = input().split()
    dic[A] = B
for i in range(M):
    C= input()
    print(dic.get(C))