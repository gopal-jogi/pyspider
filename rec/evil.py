def isevil(num):
    if num==0:
        return 0
    return num%2+isevil(num//2)
num=19    
print(isevil(num)%2==0)