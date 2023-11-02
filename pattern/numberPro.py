def prime(num):
    return 'Prime Number' if len([val for val in range(1,num+1) if num%val==0])==2 else 'Not Prime Number'

def composite(num):
    return 'Composite Number' if len([val for val in range(1,num+1) if num%val==0])>2 else 'Not Composite Number'

def perfect(num):
    return 'Perfect Number' if sum([val for val in range(1,num//2+1) if num%val==0])==num else 'Not Perfect Number'

def pronic(num):
    return 'Pronic Number' if [n*(n+1) for n in range(int(num**0.5)+1) if n*(n+1)==num]==[num] else 'Not Pronic Number'

def sunny(num):
    return 'Sunny Number' if [n**2 for n in range(1,num//2+1) if n**2==num+1]==[num+1] else 'Not Sunny Number'

def niven(num):
    return 'Niven Number' if num%sum(int(num) for num in str(num))==0 else 'Not Niven Number'

# def spy(num):
#     return sum(int(num) for num in str(num))


def armstrong(num):
    return 'Armstrong Number' if sum(int(dig)**len(str(num)) for dig in str(num))==num else 'Not Armstrong Number'

def disarium(num):
    return 'Disarium Number' if sum(list(map(lambda dig,pow:int(dig)**pow,str(num),range(1,len(str(num))+1))))==num else 'Not Disarium Number'

def pallindrom(num):
    return 'Palindrom Number' if sum(list(map(lambda dig,pow:int(dig)*10**pow,str(num),range(len(str(num))))))==num else 'Not Palindrom Number'
    # return str(num)==str(num)[::-1]

def polyprime(num):
    return "Polyprime Number" if len([val for val in range(1,num+1) if num%val==0])==2 and sum(list(map(lambda dig,pow:int(dig)*10**pow,str(num),range(len(str(num))))))==num else "Not polyprime Number"

def emrip(num):
    rev=sum(list(map(lambda dig,pow:int(dig)*10**pow,str(num),range(len(str(num))))))
    return "Emrip Number" if len([val for val in range(1,num+1) if num%val==0])==2 and rev!=num and len([val for val in range(1,rev+1) if rev%val==0])==2 else "Not Emrip Number"

def automorphic(num):
    return "Automorphic Number" if num==(num**2)%(10**len(str(num))) else "Not Automorphic Number"

def trymorphic(num):
    return "Trymorphic Number" if num==(num**3)%(10**len(str(num))) else "Not Trymorphic Number"

def tech(num):
    p=10**((len(str(num)))//2)
    return "Tech Number" if num==((num//p)+(num%p))**2 else "Not Tech Number"

def factorial(num):    
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)

def strong(num):
    return "Strong Number" if sum([factorial(int(dig)) for dig in str(num)])==num else "Not Strong Number"

def toBin(num):
    return str(num) if num<=1 else str(num%2)+toBin(num//2)

def toDec(num):
    return sum(list(map(lambda dig,p:int(dig)*(2**p),str(num),range(len(str(num))-1,-1,-1))))

def evil(num):
    return "Evil Number" if sum([int(dig) for dig in str(toBin(num))])%2==0 else "Not Evil Number"

def suqrSum(num):
    return 0 if num==0 else (num%10)**2+suqrSum(num//10)
        
def happy(num):
    return ((num if num<10 else happy(suqrSum(num)))==1)
    

if __name__=='__main__':
    print(prime(7))
    print(pronic(12))
    print(perfect(145))


# def happy(num):
#     return list(filter(lambda))

# num=

# print(list(filter(lambda num:sum([int(dig)**2 for dig in str(num) if num<10])<=9, str(num))))
# print(emrip(num))

# print(sum(list(map(lambda dig,pow:int(dig)*10**pow,str(num),range(len(str(num)))))))
# print(sum(list(map(lambda dig,ind:int(dig)**ind,str(num),range(1,len(num)+1)))))


