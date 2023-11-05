L=[10,20,30,32,49,12,13]
for ind in range(len(L)//2):
    L[ind],L[-ind-1]=L[-ind-1],L[ind]

print(L)