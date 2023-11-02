for num in range(100000,1000000):
    Copy=num
    p=(len(str(num)))//2
    rem=num%10**p
    num//=10**p
    if (rem+num)**2==Copy:
        print(Copy)
    
