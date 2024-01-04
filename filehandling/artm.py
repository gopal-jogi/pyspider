a=10
b=20
while a!=0:
    c=b&a
    b=b^a
    a=c<<1

print(b)
