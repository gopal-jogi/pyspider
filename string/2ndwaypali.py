string=input("check your string palindrom or not:- ") 
for ind in range(len(string)//2):
    if string[ind]!=string[-ind-1]:
        print('not')
        break
else:
    print('palindrom')