def isperfect(num,val):
    if val==num//2+1:
        return 0
    if num%val==0:
        return val+isperfect(num,val+1)
    return isperfect(num,val+1)
    
#     if num%val==0:
#         sum+=val
#     if val==num//2+1:
#         return 0
#     return sum+isperfect(num,val+1)
num=15
print(isperfect(num,1))
