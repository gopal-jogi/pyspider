num=int(input('Enter the number'))
Sum,product=0,1
while (num!=0):
    rem=num%10
    Sum+=rem
    product*=rem
    num//=10
print('Spy number'if (Sum==product)else 'Not Spy number')