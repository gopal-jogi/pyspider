string=input("check your check vowel string:- ")
res=''
for ch in string:
    if ch in 'AIOUEaioue':
        res+=ch
print(res)

