
def reverseWord(s,res=[],word=''):
    for ch in s:
        if ch!=' ':
            word+=ch
        else:
            res.insert(0,word)
            word=''
    res.insert(0,word)
    return ' '.join(res)
s='I am best developer'
print(reverseWord(s))
