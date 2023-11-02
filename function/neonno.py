def noNeon(num,squre,Sum=0):
    while(squre!=0):
        rem=squre%10
        Sum+=rem
        squre//=10
    return num==Sum

num=9
print(noNeon(num,num**2))