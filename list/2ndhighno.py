L=[10,12,11,12,9,12,10,8]
newL=[]
for num in L:
    if num not in newL:
        newL.append(num)
high=newL[0]
for num in newL[1:]:
    if num>high:
        high=num
print(high)
newL.remove(high)
print(L)
shigh=newL[0]
for num in newL[1:]:
    if num>shigh:
        shigh=num
print(shigh)
# L=[10,12,11,12,9,12,10,8]
# newL=list(set(L))
# high=max(newL)
# newL.remove(high)
# print(max(newL))