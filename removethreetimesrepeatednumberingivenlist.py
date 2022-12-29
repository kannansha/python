print("ENTER LIST")
l=list(map(int,input().split()))
n=len(l)
m=[]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if l[i]==l[j]:
            c+=1
    if c!=3:
        m.append(l[i])
for i in m:
    print(i,end=' ')
        
