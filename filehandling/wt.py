with open('file1.txt','a+') as f:
    f.write("i am gopal jogi\n")
    f.seek(0)
    print(f.read())