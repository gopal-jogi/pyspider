num=71
fact_count=0
for val in range(1,num+1):
    if(num%val==0):
        fact_count+=1
print('Prime number' if (fact_count==2) else 'Not prime number')