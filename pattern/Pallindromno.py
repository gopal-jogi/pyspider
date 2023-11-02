num=int(input("Enter the Number "))
Copy,res=num,0
while (num!=0):
    rem=num%10
    res=res*10+rem
    num//=10
print('Pallindrom number'if(Copy==res)else 'Not Pallindrom Number')