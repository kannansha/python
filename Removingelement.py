n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range (0,n):
    if l[i]%2==1:
        m.append(l[i])
print(m)
