#막대기

N= int(input())

N2 = bin(N)[2:]
count = 0
for i in range(len(N2)):
    if N2[i] == '1':
        count +=1
print(count)