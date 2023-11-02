def toBin(num,p):
    if num==0:
        return 0
    return (num%2)*p+toBin(num//2,p*10)
num=145
print(toBin(num,1))