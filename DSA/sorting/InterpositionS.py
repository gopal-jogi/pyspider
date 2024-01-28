L=[1,13,14,16,24,45,56]
u=100
l=0
h=len(L)-1
while l<=h and L[l]<=u<=L[h]:
    mid= int(l+((h-l)/(L[h]-L[l]))*(u-L[l]))
    if L[mid]<u:
        l=mid+1
    elif L[mid]>u:
        h=mid-1
    elif L[mid]==u:
        print(mid)
        break
else:
    print(-1)