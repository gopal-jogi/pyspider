num=145
poss=1
res=0
while (num!=0):
    rem=num%2
    res=res+(rem*poss)
    num//=2
    poss*=10
print(res)