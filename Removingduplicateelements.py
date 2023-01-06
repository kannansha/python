n = int(input())
l = list(map(int,input().split()))
u =[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
for i in u:
    print(i,end=' ')
