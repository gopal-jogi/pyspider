for num in range(100,0,-1):
    fact_count=0
    fc=0
    for val in range(1,num+1):
        if num%val==0:
            fact_count+=1
        
    if fact_count==2:
        print(num,end=' ')
        if (fc<4):
            break