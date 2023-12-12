def quick(L):
    if len(L)==0:
        return []
    p=L[0]
    le=[n for n in L[1:] if n<p]
    ri=[n for n in L[1:] if n>p]
    return quick(le)+[p]+quick(ri)
L=[4,3,2,1]
print(quick(L))