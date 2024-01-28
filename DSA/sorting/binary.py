L=[1,13,14,16,24,45,56]
u=100
l=0
h=len(L)-1
while l<=h:
    mid= (h+l)//2
    if L[mid]<u:
        l=mid+1
    elif L[mid]>u:
        h=mid-1
    elif L[mid]==u:
        print(mid)
        break
else:
    print(-1)