num=int(input("enter the number :-"))
while num>9:
    sum=0
    while num!=0:
        rem=num%10
        sum+=rem**2
        num//=10
    num=sum    
if sum==1:
    print("happy")
else:
    print("not")
