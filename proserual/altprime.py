d=0
for num in range(1,100):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                break
        else:
            d+=1
            if d%2==0:
                print(num)
                