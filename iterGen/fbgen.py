def fab(num):
    f,s=0,1
    for _ in range(num):
        yield f
        f,s=s,f+s

ob=fab(5)
for ans in ob:
    print(ans)