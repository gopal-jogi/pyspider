def merg(L,le,rig):
    ind=li=ri=0
    while li<len(le) and ri<len(rig):
        if le[li]<rig[ri]:
            L[ind]=le[li]
            ind+=1
            li+=1
        else:
            L[ind]=rig[ri]
            ind+=1
            ri+=1
    while li <len(le):
        L[ind]=le[li]
        ind+=1
        li+=1

    while ri <len(rig):
        L[ind]=rig[ri]
        ind+=1
        ri+=1
    # print(L)

def divi(L):
    if len(L)==1:
        # print(L)
        return
    le,ri=L[:len(L)//2],L[len(L)//2:]
    divi(le)
    divi(ri)
    merg(L,le,ri)

L=[4,3,2,1]
divi(L)
print(L)


