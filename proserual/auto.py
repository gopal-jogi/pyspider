num=int(input("enter the number :-"))
sqr=num**2
rem=num%(10**len(str(num)))
if num==rem:
    print("auto")
else:
    print("not")
