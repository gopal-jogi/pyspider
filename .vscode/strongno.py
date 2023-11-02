num=145
copy=num
final=0
while(num!=0):
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact*=val
    final+=fact
    num//=10
print(final)
if (copy==final):
    print('Strong Number')
else:
    print('Not Strong Number')