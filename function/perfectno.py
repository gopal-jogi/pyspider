def noPerfect(num,Sum=0):
    for v in range(1,(num//2)+1):
        if num%v==0:
            Sum+=v
    return num==Sum

num=6
print(noPerfect(num))