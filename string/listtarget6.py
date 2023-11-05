L=[1,2,3,4,5]
target=6
for ind1 in range(len(L)-1):
    for ind2 in range(ind1+1,len(L)):
        if L[ind1]+L[ind2]==6:
            print([L[ind1],L[ind2]])