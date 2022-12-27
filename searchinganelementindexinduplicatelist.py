n=int(input('Enter no.of elements:'))
l=list(map(int,input().split()))
x=int(input('Enter the search element:'))
check=0
for i in range(0,n):
    if l[i]==x:
        print(i,end=' ')
        check=check+1
if check==0:
    print('-1')
