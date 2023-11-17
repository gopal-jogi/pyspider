s=input("enter the number :-")
while s!='':
    print(f'{s[0]}={s.count(s[0])}')
    s=s.replace(s[0],'')
   
