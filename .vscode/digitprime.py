num=8732492
while(num!=0):
    rem=num%10
    fc=0
    for val in range(1,rem+1):
        if rem%val==0:
            fc+=1
    
    if fc==2:
        print(rem, end=' ')
    num//=10
