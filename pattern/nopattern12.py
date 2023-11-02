row=int(input("Enter the Row:- "))
for st in range(1,row+1):
    print(" "*(row-st),end='')
    for num in range(1,st+1):
        print(num,end='')
    print()