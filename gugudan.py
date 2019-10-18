gugudan=[]
for i in range(1,11): #10단 추가 
    temp=[]
    for j in range(1,11):
        temp.append(str((i*j)).center(4," "))
    gugudan.append(temp)
for elem in gugudan:
    print(elem)