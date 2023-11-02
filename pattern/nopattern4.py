space,count=0,5
for num in range(5,0,-1):
    print(' '*space,(str(num)+' ')*count,sep='')
    space+=1
    count-=1