def isArmstrong(num,p):
    if num==0:
        return 0
    return (num%10)**p+isArmstrong(num//10,p)
num=372
if isArmstrong(num,len(str(num)))==num:
    print("Armstrong")
else:
    print("Not Armstrong")