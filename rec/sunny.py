def isSunny(num,n):
    if n**2>num+1:
        return False
    if n**2==num+1:
        return True
    return isSunny(num,n+1)
num=24
print("Sunny"if isSunny(num,1) else "not sunny")
#     print("Sunny")
# else:
#     print('Not Sunny')