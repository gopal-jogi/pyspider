L=[17,15,12,11,10]
for ti in range(1,len(L)):
    li=ti
    val=L[ti]
    while li>0 and val < L[li-1]:
        L[li]=L[li-1]
        li-=1
    L[li]=val
print(L)