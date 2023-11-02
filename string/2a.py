s="2a 3d 4a 1d"
res=''
for i in s.split():
    res+=int(i[0])*i[1]
print(res)
