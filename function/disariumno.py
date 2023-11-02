def noDisarium(num,Copy,Sum=0):
    while(num!=0):
        rem=num%10
        Sum+=rem**len(str(num))
        num//=10
    return Copy==Sum
num=135
print(noDisarium(num,num))