def cv(s,c=0,res=''):
    if c== len(s):
        return res
    if s[c] not in res:
        res+=s[c]
        return cv(s,c+1,res=res)
    return cv(s,c+1,res)


s=input("enter the string:- ")

print(cv(s))