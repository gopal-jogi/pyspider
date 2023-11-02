space=3
for star in range(1,8,2):
    print(' '*space,'*'*star,sep='')
    space-=1
space=1
for star in range(5,0,-2):
    print(' '*space,'*'*star,sep='')
    space+=1

