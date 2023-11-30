n = int(input())
s = set(map(int, input().split()))
num=int(input())
for _ in range(num):
    com=input().split()
    if com[0]=='pop':
        s.pop
    elif com[0]=='remove':
        s.remove(int(com[1]))
    else:
        s.discard(int(com[1]))
print(sum(s))