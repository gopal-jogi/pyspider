def sea(L,t,ind):
    if len(L)==ind:
        return -1
    elif L[ind]==t:
        return ind
    return sea(L,t,ind+1)

L=[4,5,6,7,0,1,2]
t=3
print(sea(L,t,0))