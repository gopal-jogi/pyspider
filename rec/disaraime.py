def isDisariam(num,p):
    if num==0:
        return 0
    return (num%10)**p+isDisariam(num//10,p-1)
num=136
if isDisariam(num,len(str(num)))==num:
    print('Disarime')
else:
    print('Not Disarime')