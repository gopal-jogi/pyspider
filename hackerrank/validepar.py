def valid(s):
    while s!='':
        if '()' in s:
            s=s.replace('()','')
        elif '[]' in s: 
            s=s.replace('[]','')  
        elif '{}' in s:
            s=s.replace('{}','')
            
        else:
            return False
    return True
    
s='([])'
print(valid(s))
