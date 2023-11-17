def cv(s,c=0):
    for ch in s:
        if ch in 'aeiouAEIOU':
            c+=1
    return c
print(cv(input('entre the string')))
