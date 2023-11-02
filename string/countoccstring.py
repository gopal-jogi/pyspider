string=input("check your occurnace charecte in given string :- ")
ch=0
while string!='':
    print(f'{string[ch]}-{string.count(string[ch])}')
    string=string.replace(string[ch],'')
    
