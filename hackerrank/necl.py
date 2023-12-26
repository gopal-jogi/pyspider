def sor(L,tar):
    # for ind in range(len(L)):
    #     if tar >L[ind]:
    #         pass
    #     else:
    #         L.insert(ind,tar)
    #         print(ind)
    #         break
    # else:
    #     print(ind)
    f=L+[tar]
    f.sort()
    print(f.index(tar))
L=[1]
tar=10
sor(L,tar)