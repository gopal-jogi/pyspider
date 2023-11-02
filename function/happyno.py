def happyNo(num):
    while(num>9):
        res=0
        while(num!=0):
            rem=num%10
            res+=rem**2
            num//=10
        num=res
    return num==1


print(happyNo(91))