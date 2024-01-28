n=7
sp=n//2
s=1
for i in range(n):
    num=1
    for j in range(sp):
        print(' ',end='')
    for x in range(s):
        print(num,end='')
        if x<s//2:
            num+=1
        else:
            num-=1
    if i < n//2:
        sp-=1
        s+=2
    else:
        sp+=1
        s-=2
    print()