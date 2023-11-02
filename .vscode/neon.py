num=33
pow=num**2
sum=0
while(pow!=0):
    rem=pow%10
    sum+=rem
    pow//=10
if(num==sum):
    print('Neon number')
else:
    print('Not Neon Number')    