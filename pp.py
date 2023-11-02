L=[10,12,3,8,12,5,12,11]
newL=list(set(L))
m=max(newL)
newL.remove(m)
print(max(newL))