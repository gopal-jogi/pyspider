from itertools import permutations as p
L=[1]
# print(list(map(list,p(L))))
print([list[val] for val in p(L)])