def lent(s):
    s=s.lstrip()
    l=s.split()
    return len(l[-1])


s="Hello   world   "
print(lent(s))