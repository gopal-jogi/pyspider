n=7
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n-1 or j==0:
            print('@',end='')
        elif i==j==n//2:
            print('A',end='')
        else:
            print(' ',end='')
    print()