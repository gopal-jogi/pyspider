def single_ton(cls):
    L=[]
    def inner():
        if len(L)==0:
            obj=cls()
            L.append(obj)
        return L[0]
    return inner

  
class abc:
    def __init__(self):
        print("hello word")
s1=abc()
s2=abc()
print(s1)
print(s2)
