def noComposite(num,fc=0):
    for v in range(1,num+1):
        if num%v==0:
            fc+=1
    return fc>2

num=18
print(noComposite(num))