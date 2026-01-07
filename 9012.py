N = int(input())
for _ in range(N):
    A= input()
    stack = []
    for j in A:
        if j =='(':
            stack.append(j)
        elif j ==')':
            if stack==[]:
                print('NO')
                break
            else:
                stack.pop()
    else :
        if stack == [] :
            print('YES')
        else:
            print('NO')

