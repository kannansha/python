n=int(input())
m=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input('Enter the value:'))
        l.append(x)
    m.append(l)
for res in m:
    print(res)
s1=0
s2=0
for i in range(n):
    for j in range(n):
        if(i==j):
            s1=s1+m[i][j]
        if(i+j==n-1):
            s2=s2+m[i][j]
if(s1>s2):
    dif=s1-s2
else:
    dif=s2-s1
print('difference between left and right diagonals:',dif)
            
