#암호 만들기
def dfs(start):
    if len(li) == N:
        A = 0
        B = 0
        for i in li:
            if i in 'aeiou':
                A += 1
            else:
                B += 1
        if A >= 1 and B >= 2:
            print("".join(li))
        return

    for i in range(start, M):
            li.append(key[i])
            dfs(i+1)
            li.pop()
            # print(li)

N , M = map(int, input().split())
key = list(input().split())
key.sort()
li= []
dfs(0)
# for i in range(M):
#     if li[i] == 'a'or 'i' or 'e' or 'o' or 'u':

