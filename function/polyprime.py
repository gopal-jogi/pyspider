def noPolyprime(num,Copy,rev=0,fc=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    for v in range(1,Copy+1):
        if (Copy%v==0):
            fc+=1
    return Copy==rev and fc==2
num=11
print(noPolyprime(num,num))