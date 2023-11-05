s='engineering'
newS=''
for ch in s:
    if ch not in newS:
        newS+=ch
for ch in newS:
    print(f'{ch}={s.count(ch)}')
