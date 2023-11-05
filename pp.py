s='malalam'
newS=''
li=-1
for ch in range(len(s)//2):
    if s[ch]==s[li]:
        li-=1
    else:
        print('not')
        break
else:
    print('palindrom' )