def pali(s):
    import re
    s=s.lower()
    # ns=''
    # for ch in s:
    #     if ch.isalnum():
    #         ns+=ch
    # return ns==ns[::-1]
    s=re.findall('\w',s)
    return s==s[::-1]
s="ab a"
print(pali(s))