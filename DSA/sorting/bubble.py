L=[17,15,12,11,10]
for ev in range(len(L)-1,0,-1):
    for ind in range(ev):
        if L[ind]>L[ind+1]:
            L[ind],L[ind+1]=L[ind+1],L[ind]
print(L)


