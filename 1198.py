    #삼각형으로 자르기

    N = int(input())
    li_X = []
    li_Y = []
    for _ in range(N):
        X, Y = map(int, input().split())
        li_X.append(X)
        li_Y.append(Y)
    MAX= 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                area = 1/2 *abs(((li_X[i] * li_Y[j] + li_X[j] * li_Y[k] + li_X[k] * li_Y[i]) - (li_X[j] * li_Y[i] +li_X[k] * li_Y[j] + li_X[i] * li_Y[k]) ))
                if area >= MAX:
                    MAX = area
    print(MAX)

