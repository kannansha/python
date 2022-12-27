n=int(input('Enter no.of elements:'))
l=list(map(int,input().split()))
x=int(input('Enter the search element:'))
low=0
high=n-1
mid=(high+low)//2
flag=0
while high>=low:
    if x>l[mid]:
        low=mid+1
    elif x==l[mid]:
        flag=1
        break
    else:
        high=mid+1
    mid=(high+low)//2
if flag==1:
    print('Element is found',mid,'index location')
else:
    print('Element is not found')
