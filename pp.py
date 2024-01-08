def fa(n,f=1):
    while n>0:
        f*=n
        n-=1
    return f
n=5
print(fa(n))