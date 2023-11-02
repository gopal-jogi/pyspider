def noAutomorphic(num,squr,p):
    # squr=num**2
    rem=squr%10**p
    return num==rem
     
num=125
# squr=num**2
print(noAutomorphic(num,num**2,len(str(num))))