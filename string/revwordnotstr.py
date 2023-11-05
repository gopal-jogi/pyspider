s='we are groot'
L=[]
for word in s.split():
    L.append(word[::-1])
print(' '.join(L))