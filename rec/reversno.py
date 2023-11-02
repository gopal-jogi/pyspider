def isReverno(num,p):
    if num==0:
        return 0
    return num%10 *10**p+isReverno(num//10,p-1)
num=121
if (isReverno(num,len(str(num))-1))==num:
    print("palindrom")
else:
    print("Not Palindrom")