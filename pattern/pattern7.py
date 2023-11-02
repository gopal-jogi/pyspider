row=int(input("Enter the Row:- "))
sp=row-1
sp1=row-row
for star in range(1,row*2,2):
    print(" "*sp,"*"*star,sep="")
    sp-=1
for star in range(((row-1)*2)+1,0,-2):
    print(" "*sp1,"*"*star,sep="")
    sp1+=1

