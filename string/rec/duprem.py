def dupRem(s,ind,ns=''):
    if len(s)==ind:
        return ns
    if s[ind] not in ns:
        ns+=s[ind]
    return dupRem(s,ind+1,ns=ns)

a = "enginerring"
print(dupRem(a,0))

