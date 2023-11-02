def noStrong(num,Copy,Sum=0):
    while (num!=0):
        rem=num%10
        res=1
        for v in range(1,rem+1):
            res*=v
        Sum+=res
        num//=10
    return Copy==Sum    
num=145
print(noStrong(num,num))