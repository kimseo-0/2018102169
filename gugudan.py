gugudan=[]
for i in range(1,10):
    temp=[]
    for j in range(1,10):
        temp.append(str((i*j)).center(4," "))
    gugudan.append(temp)
for elem in gugudan:
    print(elem)