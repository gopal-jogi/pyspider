n=0
c=0
while True:
    n+=1
    if n>1:
        for v in range(2,n//2+1):
            if n%v==0:
                break
        else:
            print(n)
            c+=1
            if c==3:
                break