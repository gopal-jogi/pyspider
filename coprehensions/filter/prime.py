print(list(filter(lambda num:len([val for val in range(1,num+1) if num%val==0])==2 ,[11,13,8,9,5,2,1])))
