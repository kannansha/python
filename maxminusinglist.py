n=int(input('Enter the no.of elements:'))
l=list(map(int,input().split()))
max=l[0]
min=max
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print('minimum number:',min,end='\n')
print('maximum number:',max,end=' ')
