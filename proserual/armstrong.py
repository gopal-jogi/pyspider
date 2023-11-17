num=int(input("enter the number :-"))
Copy=num
p=len(str(num))
sum=0
while num!=0:
    rem=num%10
    sum+=rem**p
    num//=10
if Copy==sum:
    print("armstrong")
else:
    print("not")