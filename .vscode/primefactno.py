num=56
for fact in range(1,num+1):
    if num%fact==0:
        fc=0
        for val in range(1,fact+1):
            if fact%val==0:
                fc+=1
        if fc==2:
            print(fact)