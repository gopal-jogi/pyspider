def single_ton(cls):
    L=[]
    def inner():
        if len(L)==0:
            obj=cls()
            L.append(obj)
        return L[0]
    return inner

@single_ton
class mno:
    def __init__(self):
        print("hello word")

s1=mno()
s2=mno()
s3=mno()
print(s1)
print(s2)
print(s3)