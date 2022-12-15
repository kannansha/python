n=int(input('Enter no.of elements:'))
l=list(map(int,input().split()))
t=int(input('Enter the target value:'))
c=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if l[i]>l[j]:
            if(l[i]-l[j]==t):
                c=1
                break
        else:
            if(l[j]-l[i]==t):
                c=1
                break
if c==1:
    print('YES')
else:
    print('NO')
            
