r=int(input('Enter no.of rows:'))
c=int(input('Enter no.of columns:'))
m=[]
for i in range(0,r):
    l=[]
    for j in range(0,c):
        x=int(input('Enter the value:'))
        l.append(x)
    m.append(l)
for res in m:
    print(res)
for i in range(0,r):
    for j in range(0,c):
        if i==j:
            print(m[i][j],end=' ')
