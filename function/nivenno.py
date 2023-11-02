def nivenNo(num,copy,sum=0):
    while num!=0:
        rem=num%10
        sum+=rem
        num//=10
    return copy%sum==0
num=100
print(nivenNo(num,num))