def isB2D(bin,p=1,Sum=0):
    while(bin!=0):
        rem=bin%10
        Sum+=rem*p
        bin//=10
        p*=2
    return Sum

bin=100111
print(isB2D(bin))