def isniven(num):
    if num==0:
        return 0
    return num%10+isniven(num//10)
num=14
print(num%isniven(num)==0)