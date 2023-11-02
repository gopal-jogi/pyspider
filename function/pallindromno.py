def noPallindrom(num,Copy,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return Copy==rev
    
num=121
print(noPallindrom(num,num))