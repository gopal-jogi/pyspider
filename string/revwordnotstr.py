s='we are groot'
# L=[]
# for word in s.split():
#     L.append(word[::-1])
# print(' '.join(L))
revW=''
newS=''
for ch in s:
    if ch!=' ':
        revW=ch+revW
    else:
        newS+=revW+ ' '
        revW=''
newS+=revW
print(newS)
