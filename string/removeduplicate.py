string=input("check your remove duplicate in string:- ") 
res=''
for ch in string:
    if ch not in res:
        res+=ch
print(res)