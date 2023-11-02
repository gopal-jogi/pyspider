def noEvil(num,Sum=0):
    while(num!=0):
        rem=num%2
        Sum+=rem
        num//=2
    return Sum%2==0
num=17
print(noEvil(num))