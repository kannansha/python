s=input()
n=len(s)
k=0
c=1
res=''
for i in range(1,n):
    if s[i]==s[k]:
        c=c+1
    else:
        res=res+str(c)+s[k]
        k=i
        c=1
    if i==n-1:
        res=res+str(c)+s[k]
print(res)
