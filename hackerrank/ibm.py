def count_triplets(arr, n, d):
    from itertools import combinations as c
    co=0
    for el in c(arr,3):
        if sum(el)%d==0:
            co+=1
    return co
# Example
a = [3,3,4,7]
d =5
result = count_triplets(a, len(a), d)
print(result)