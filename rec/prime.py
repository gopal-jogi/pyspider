def isPrime(num,val):
    # if num!=2 and num!=3:
    if val==int(num*0.5+1):
    # if val==num//2+1:
        return True
    if num%val==0 or num<2:
        return False
    # if val==int(num*0.5+1):
    #     return True
    return isPrime(num,val+1)
    # else:
    #     return True
num=97

if isPrime(num,2):
    print('Prime')
else:
    print('Composite')