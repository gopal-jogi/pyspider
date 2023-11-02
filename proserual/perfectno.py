num=6
fact_count=0
for value in range(1,num//2+1):
    fact_count+=value
print('perfect number'if (num==fact_count) else 'Not perfect number')