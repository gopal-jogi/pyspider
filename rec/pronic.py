def isPronic(num,n):
    if n*(n+1)>num:
        return False
    if n*(n+1)==num:
        return True
    return isPronic(num,n+1)
num=13
print(isPronic(num,1))