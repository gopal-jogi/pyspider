def is_prime(num, val=2):
    if val==num//2+1:
        return True
    if num % val == 0 or num < 2:
        return False
    return is_prime(num, val + 1)

def altPrime(s=1, e=15, even=True):
    if s <= e:
        if is_prime(s):
            if even:
                print(s)
            altPrime(s + 1, e, not even)
        else:
            altPrime(s + 1, e, even)

altPrime()
