def isSuqrsum(num):
    if num==0:
        return 0
    return (num%10)**2+isSuqrsum(num//10)
def isHappy(num):
    if num<10:
        return num
    return isHappy(isSuqrsum(num))
num=13
if isHappy(num)==1:
    print('Happy')
else:
    print("Not Happy")