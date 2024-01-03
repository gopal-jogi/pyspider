def dup(nums):
    for el in nums:
        if 2<= nums.count(el):
            return True
    return False

nums=[]
print(dup(nums))