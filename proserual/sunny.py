num=int(input("enter the number :-"))
n=0
while n**2<=num+1:
    if n**2==num+1:
        print("sunny")
        break
    else:
        n+=1
else:
    print("not")
    