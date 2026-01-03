    # 더하기 사이클

    N = int(input())
    answer = N
    count = 0
    while  1:
        count += 1
        A = N//10
        B = N%10

        X =A + B
        C = X%10
        N = B*10 + C
        if N == answer:
            print(count)
            break



