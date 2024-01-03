nums=[1,2,2,1,2,2,2,2]
res=nums.count(max(nums,key=lambda a: [nums.count(a)]))
print(res if res>len(nums)/2 else 0)