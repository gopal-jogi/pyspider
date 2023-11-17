num=int(input("enter the number :-"))
Copy=num
p=len(str(num))
sum=0
while num!=0:
    rem=num%10
    sum+=rem**p
    num//=10
    p-=1
if Copy==sum:
    print("disarium")
else:
    print("not")
