num=int(input('Enter the number'))
Copy=num
Sum=0
while (num!=0):
    rem=num%10
    Sum+=rem
    num//=10
print('Nevien number'if (Copy%Sum==0)else 'Not Nevien number')