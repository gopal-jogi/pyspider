def noSunny(num,n=0):
    while(n**2<=num+1):
        if n**2==num+1:
            return True
        n+=1
    return False
        

num=8
print(noSunny(num))