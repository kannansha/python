n=int(input('Enter no.of elements:'))
ol=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,n):
    if ol[i]%2==0:
        l1.append(ol[i])
    else:
        l2.append(ol[i])
l=l1+l2
for i in range(n):
    print(l[i],end=' ')
