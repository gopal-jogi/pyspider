def isprime(num,val=2):
    if num//2+1 == val:
        return True
    if num%val==0 or num<2:
        return False
    return isprime(num,val+1)

def evenprime(num=1,end=15,e=True):
    if num<=end:
        
        if isprime(num):
            if e:
                print(num)
            return evenprime(num+1,end,not e)
        else:
            return evenprime(num+1,end,e)
    
evenprime()
    