def isNeon(squr):
    if squr==0:
        return 0
    return squr%10+isNeon(squr//10)
num=10
if isNeon(num**2)==num:
    print('Neon')
else:
    print('Not Neon')
