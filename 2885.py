# 초콜릿 식사
N= int(input())
N2= bin(N)[2:] ## 2진수변환
Hap = 0        ## 2의제곱수판단
li=[]
for i in range(len(N2)):  ##2진수에서 1찾기
    if N2[i] == '1':
        Hap += 1
        li.append(i)     ## 1 자릿수 list추가
if Hap == 1:             ## 2의제곱수이면
    print(2**(len(N2)-1), end=' ')  ## 크기에서 1빼고 출력
    print(0)                        ## 0출력
else:
    print(2**(len(N2)), end=' ')
    li.sort(reverse=True)
    print(li[0]+1)                  ## 마지막1의 수에+1만큼 초콜릿을 쪼개야함.