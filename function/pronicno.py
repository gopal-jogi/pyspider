def noPronic(num,n=0):
    while(n*(n+1)<=num):
        if n*(n+1)==num:
            return True
        n+=1
    return False
    
num=31
print(noPronic(num))