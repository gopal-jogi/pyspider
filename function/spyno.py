def noSpy(num,Sum=0,pro=1):
    while(num!=0):
        rem=num%10
        pro*=rem
        Sum+=rem
        num//=10
    return pro==Sum
num=214
print(noSpy(num))