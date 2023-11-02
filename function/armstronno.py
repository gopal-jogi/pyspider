def armstrongNo(num,copy,p,sum=0):
    while num!=0:
        rem=num%10
        sum+=rem**p
        num//=10
    return copy==sum
num=356
print(armstrongNo(num,num,len(str(num))))