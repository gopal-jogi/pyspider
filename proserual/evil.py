num=int(input("enter the number :-"))
sum=0
while num!=0:
    rem=num%2
    sum+=rem
    num//=2
    
if sum%2==0:
    print("evil")
else:
    print("not")
