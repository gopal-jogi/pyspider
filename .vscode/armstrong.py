for num in range(1000,10000):
    p=len(str(num))
    Copy=num
    Sum=0
    while(num!=0):
        rem=num%10
        Sum=Sum+(rem**p)
        num//=10
    if(Copy==Sum):
        print(Sum ,end=' ')
    