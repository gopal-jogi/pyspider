def isTech(num,p):
    if num==0:
        return 0
    return num%p+isTech(num//p,p)
num=2020
if isTech(num,10**(len(str(num))//2))**2==num:
    print("Tech")
else:
    print("Not Tech")