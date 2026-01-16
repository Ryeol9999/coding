#화학식량
Name = input()
stack = [[ ]]
count = 0
for i in range(len(Name)):
    if Name[i] == "(":
        stack.append([])
        count +=1
    elif Name[i] == ")":
        X = stack.pop()
        if count != 0:
            stack[count].append(X)
        for i in range(len(X)):


    elif Name[i] == "H":
        stack[count].append(i)
    elif Name[i] == "C":
        stack[count].append(i)
    elif Name[i] == "O":
        stack[count].append(i)
    else:
        stack[count].append(i)

# stack 이라는 리스트생성
#  '(' 입력받으면 count +1 하고 stack 리스트에 빈 리스트 append
#  ')' 입력받으면 count -1 하고 stack 에있는 리스트 pop
#  count 가 0 이 아니면 list