Sum=0
for num in range(1,100):
    fact_sum=0
    for val in range(1,(num//2)+1):
        if (num%val==0):
            fact_sum+=val
    
    if num==fact_sum:

       Sum+=num
print(Sum)
