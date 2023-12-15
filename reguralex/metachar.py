import re
s='aec!2 $\t\n *jjj'
s1='g gd god good goood'
s2='This is a regular exprestion practice 1234 @#$^'
# print(re.findall('.',s))
# print(re.findall('^g g',s1))
# print(re.search('^g g',s1))
# print(re.findall('ood$',s1))
print(re.findall('go*d',s1))
# print(re.findall('go+d',s1))
# print(re.findall('go?d',s1))
# print(re.findall('gd|good|go',s1))
# print(re.findall('go{1}d',s1))
# print(re.findall('go{0,4}d',s1))
# print(re.findall('[aieouAEIOU]',s2))
# print(re.findall('[^aieouAEIOU]',s2))
# print(re.findall('[0-9 a-z A-Z \^ ]',s2))
