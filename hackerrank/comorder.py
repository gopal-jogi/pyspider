from itertools import combinations as c
n=4
k=3
num=[val for val in range(1,n+1)]
print([list(val) for val in list(c(num,k))])