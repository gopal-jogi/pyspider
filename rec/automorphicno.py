def isAutomorphic(num,squr):
    if num==0:
        return True
    if num%10!=squr%10:
        return False
    return isAutomorphic(num//10,squr//10)
num=7
print("Automorphic number"if isAutomorphic(num,num**2) else "Not Automorphic")
