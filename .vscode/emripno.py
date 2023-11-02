num=19
copy=num
rev=0
fact_count,fact_count1=0,0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
for val in range(1,copy+1):
    if(copy%val==0):
        fact_count+=1
for value in range(1,rev+1):
    if(rev%value==0):
        fact_count1+=1
if(copy!=rev and fact_count==2 and fact_count1==2):
    print('This is emrim number')
else:
    print('This is not emrim number')