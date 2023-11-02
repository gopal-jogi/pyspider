def isfact(num):
    if num==1 or num==0:
        return 1
    return num*isfact(num-1)
def isStrong(num):
    if num==0:
        return 0
    return isfact(num%10)+isStrong(num//10)
num=145
if isStrong(num)==num:
    print("strong")
else:
    print("Not strong")
