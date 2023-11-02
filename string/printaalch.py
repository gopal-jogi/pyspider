string=input("check your charecter in string :- ") 
up,lc,dig,sp='','','',''
for ch in string:
    if 'A'<=ch<='Z':
        up+=ch
    elif 'a'<=ch<='z':
        lc+=ch
    elif '0'<=ch<='9':
        dig+=ch
    else:
        sp+=ch
print(up,lc,dig,sp)
