n=int(input())
A=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):
        x=int(input())
        l.append(x)
    A.append(l)
k=int(input())
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            A[i][j]=k
        else:
            A[i][j]=0
print("Updated matrix:")
for i in range(0,n):
    for j in range(0,n):
        print(A[i][j],end=' ')
    print( )
