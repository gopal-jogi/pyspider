L=[10,12,13,10,12,14,12]
newL=[]
for num in L:
    if num not in newL:
        newL.append(num)
print(newL)