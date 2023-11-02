def isPalindrom(num,p):
    if num==0:
        return 0
    return (num%10)*10**p+isPalindrom(num//10,p-1)
def isPrime(num,val):
    if val==num//2+1:
        return True
    if num%val==0 or num<2:
        return False
    return isPrime(num,val+1)
def isRevPrime(rev,val):
    if val==rev//2+1:
        return True
    if rev%val==0 or rev<2:
        return False
    return isRevPrime(rev,val+1)

num=12
if isPalindrom(num,len(str(num))-1)!=num and isRevPrime(isPalindrom(num,len(str(num))-1),2) and isPrime(num,2):
    print("Emrip")
else:
    print('Not Emrip')