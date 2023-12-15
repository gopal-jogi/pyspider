L=[17,15,12,11,10]
for ti in range(len(L)-1):
    li=ti
    for ind in range(ti+1,len(L)):
        if L[li]>L[ind]:
            li=ind
    L[li],L[ti]=L[ti],L[li]

print(L)