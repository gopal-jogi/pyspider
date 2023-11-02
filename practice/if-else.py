a=10
b=30
c=47
d=5
if (a>b):
    if (a>c):
        if(a>d):
            print('a is highest')
        else:
            print('d is highest')
    else:
        if(c>d):
            print('c is higest')
        else:
            print('d is highest')
else:
    if(b>c):
        if(b>c):
            print('b is highest')
        else:
            print('d is highest')
    else:
        if(c>d):
            print('c is highest')  
        else:
            print('d is highest')