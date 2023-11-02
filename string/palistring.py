string=input("check your string palindrom or not:- ") 
res=''
for ind in range(-len(string),0):
    res+=string[ind]
print(res)
print("palindrom" if string==res else "not")