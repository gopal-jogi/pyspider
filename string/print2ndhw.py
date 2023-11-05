L=[10,12,3,8,12,5,12,11]
newL=[]
for val in L:
    if val not in newL:
        newL.append(val)
high=newL[0]
for val in newL[1:]:
    if high<val:
        high=val
newL.remove(high)
high2=newL[0]
for val in newL[1:]:
    if high2<val:
        high2=val
print(high2)