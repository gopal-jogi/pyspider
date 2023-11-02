L=[]
for num in range(1,15):
    count=0
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    if count==2:
        L.append(num)
for num in L[::2]:
    print(num)