n=int(input('Enter no.of elements:'))
l=list(map(int,input().split()))
x=int(input('Enter the search element:'))
if x in l:
    print('Element is found',end=' ')
    print('located at',l.index(x))
else:
    print('Element is not found')
