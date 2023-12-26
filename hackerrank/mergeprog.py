def merg(n1,m,n2,n):
    for ind in range(-1,-n-1,-1):
        n1[ind]= n2[ind]
    n1.sort()
    print(n1)


n1=[1,2,3,0,0,0]
n2=[2,5,6]
m=3
n=3
merg(n1,m,n2,n)