def noTech(num,Copy,p):
    rem=num%p
    num//=p
    return (num+rem)**2==Copy
    

num=2025
print(noTech(num,num,10**((len(str(num)))//2)))