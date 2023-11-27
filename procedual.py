c=0
target =-2
nums=[-6,2,5,-2,-7,-1,3]

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        a= nums[i] + nums[j]
        if a<target:
            c+=1
    print(c)