def cv(s,ind,uc='',lc='',dig='',sp=''):
    if ind==len(s):
        return uc,lc,dig,sp
    elif 'A'<=s[ind]<='Z':
        uc+=s[ind]
    elif 'a'<=s[ind]<='z':
        lc+=s[ind]
    elif '0'<=s[ind]<='9':
        dig+=s[ind]
    else:
        sp+=s[ind]
    return cv(s,ind+1,uc=uc,lc=lc,dig=dig,sp=sp)

s=input("enter the string:- ")
print(' '.join(cv(s,0)))