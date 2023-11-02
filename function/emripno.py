def noEmrip(num,Copy,rev=0,fc=0,fv=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    for v in range(1,Copy+1):
        if (Copy%v==0):
            fc+=1
    for v in range(1,rev+1):
        if (rev%v==0):
            fv+=1
    return Copy!=rev and fc==2 and fv==2
num=81
print(noEmrip(num,num))