num=int(input("enter the number :-"))
Copy=num
sum=0
while num!=0:
    rem=num%10
    sum=sum*10+rem
    num//=10
    
if Copy==sum:
    print("palindrom")
else:
    print("not")
