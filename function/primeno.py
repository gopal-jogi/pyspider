def noPrime(num,fc=0):
    for v in range(1,num+1):
        if (num%v==0):
            fc+=1
    if fc==2:
        return "prime"
    return "not"
num=12 
print(noPrime(num))