n=int(input('Enter no.of elements:'))
l=list(map(int,input().split( )))
m=[]
for i in l:
    if i not in m:
        m.append(i)
if l!=m:
    print('YES')
else:
    print('NO')
