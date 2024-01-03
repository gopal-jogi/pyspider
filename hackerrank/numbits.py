from math import factorial as f
def fact(n):
    res=str(f(n))
    c=0
    for v in range(-1,-len(res)-1,-1):
        if res[v]=='0':
            c+=1 
        else: 
            return c      
    
    # c=0
    # while True:
    #     if res%10==0:
    #         c+=1
    #         res//=10
    #     else:
    #         return c
    


print(fact(10))